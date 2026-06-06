"""
Kargah API — FastAPI backend
Two-sided marketplace: Masters (Ustads) ↔ Seekers

Run with:  uvicorn main:app --reload
Docs at:   http://127.0.0.1:8000/docs
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import database

app = FastAPI(
    title="Kargah API",
    description="Two-sided marketplace connecting Iranian craft masters with learners",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    database.init_db()


# ---------------------------------------------------------------------------
# Pydantic models
# ---------------------------------------------------------------------------

class CategoryOut(BaseModel):
    id: int
    name: str
    name_fa: str
    emoji: Optional[str] = "🎨"


class MasterOut(BaseModel):
    id: int
    name: str
    bio: Optional[str] = None
    city: Optional[str] = None
    category_id: Optional[int] = None
    category_name: Optional[str] = None
    category_name_fa: Optional[str] = None
    category_emoji: Optional[str] = None
    image_url: Optional[str] = None
    contact_email: Optional[str] = None
    years_exp: Optional[int] = None


class MasterCreate(BaseModel):
    name: str
    bio: Optional[str] = None
    city: Optional[str] = None
    category_id: Optional[int] = None
    image_url: Optional[str] = None
    contact_email: Optional[str] = None
    years_exp: Optional[int] = None


class SessionOut(BaseModel):
    id: int
    master_id: int
    master_name: Optional[str] = None
    master_city: Optional[str] = None
    category_emoji: Optional[str] = None
    title: str
    description: Optional[str] = None
    type: str            # 'studio' | 'mobile' | 'commission'
    duration_hr: Optional[float] = None
    price_range: Optional[str] = None
    max_people: Optional[int] = None


class SessionCreate(BaseModel):
    master_id: int
    title: str
    description: Optional[str] = None
    type: str
    duration_hr: Optional[float] = None
    price_range: Optional[str] = None
    max_people: Optional[int] = 1


class BookingRequestCreate(BaseModel):
    session_id: int
    seeker_name: str
    seeker_email: str
    message: Optional[str] = None


# ---------------------------------------------------------------------------
# Routes — Public
# ---------------------------------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "Welcome to Kargah API",
        "docs": "http://127.0.0.1:8000/docs",
    }


@app.get("/categories", response_model=List[CategoryOut])
def get_categories():
    conn = database.get_connection()
    rows = conn.execute("SELECT * FROM categories ORDER BY name").fetchall()
    conn.close()
    return [dict(r) for r in rows]


@app.get("/masters", response_model=List[MasterOut])
def get_masters(
    category_id: Optional[int] = None,
    city: Optional[str] = None,
    search: Optional[str] = None,
):
    conn = database.get_connection()
    query = """
        SELECT m.*, c.name AS category_name, c.name_fa AS category_name_fa, c.emoji AS category_emoji
        FROM masters m
        LEFT JOIN categories c ON m.category_id = c.id
        WHERE 1=1
    """
    params: list = []

    if category_id:
        query += " AND m.category_id = ?"
        params.append(category_id)
    if city:
        query += " AND m.city LIKE ?"
        params.append(f"%{city}%")
    if search:
        query += " AND (m.name LIKE ? OR m.bio LIKE ?)"
        params.extend([f"%{search}%", f"%{search}%"])

    query += " ORDER BY m.name"
    rows = conn.execute(query, params).fetchall()
    conn.close()
    return [dict(r) for r in rows]


@app.get("/masters/{master_id}", response_model=MasterOut)
def get_master(master_id: int):
    conn = database.get_connection()
    row = conn.execute(
        """
        SELECT m.*, c.name AS category_name, c.name_fa AS category_name_fa, c.emoji AS category_emoji
        FROM masters m
        LEFT JOIN categories c ON m.category_id = c.id
        WHERE m.id = ?
        """,
        (master_id,),
    ).fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Master not found")
    return dict(row)


@app.get("/masters/{master_id}/sessions", response_model=List[SessionOut])
def get_master_sessions(master_id: int):
    conn = database.get_connection()
    rows = conn.execute(
        """
        SELECT s.*, m.name AS master_name, m.city AS master_city, c.emoji AS category_emoji
        FROM sessions s
        JOIN masters m ON s.master_id = m.id
        LEFT JOIN categories c ON m.category_id = c.id
        WHERE s.master_id = ?
        ORDER BY s.type
        """,
        (master_id,),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


@app.get("/sessions", response_model=List[SessionOut])
def get_sessions(
    type: Optional[str] = None,
    category_id: Optional[int] = None,
    city: Optional[str] = None,
):
    """
    Browse all sessions.
    - type: 'studio', 'mobile', or 'commission'
    - category_id: filter by craft category
    - city: filter by master's city
    """
    conn = database.get_connection()
    query = """
        SELECT s.*, m.name AS master_name, m.city AS master_city, c.emoji AS category_emoji
        FROM sessions s
        JOIN masters m ON s.master_id = m.id
        LEFT JOIN categories c ON m.category_id = c.id
        WHERE 1=1
    """
    params: list = []

    if type:
        query += " AND s.type = ?"
        params.append(type)
    if category_id:
        query += " AND m.category_id = ?"
        params.append(category_id)
    if city:
        query += " AND m.city LIKE ?"
        params.append(f"%{city}%")

    query += " ORDER BY s.type, m.name"
    rows = conn.execute(query, params).fetchall()
    conn.close()
    return [dict(r) for r in rows]


@app.post("/booking-requests", status_code=201)
def create_booking_request(data: BookingRequestCreate):
    conn = database.get_connection()
    # Verify the session exists
    session = conn.execute("SELECT id FROM sessions WHERE id = ?", (data.session_id,)).fetchone()
    if not session:
        conn.close()
        raise HTTPException(status_code=404, detail="Session not found")

    conn.execute(
        "INSERT INTO booking_requests (session_id, seeker_name, seeker_email, message) VALUES (?, ?, ?, ?)",
        (data.session_id, data.seeker_name, data.seeker_email, data.message),
    )
    conn.commit()
    conn.close()
    return {"message": "Booking request submitted successfully"}


# ---------------------------------------------------------------------------
# Routes — Admin (Week 9–10: uncomment these after finishing the public routes)
# ---------------------------------------------------------------------------

# @app.post("/masters", response_model=MasterOut, status_code=201)
# def create_master(data: MasterCreate):
#     conn = database.get_connection()
#     cursor = conn.cursor()
#     cursor.execute(
#         "INSERT INTO masters (name, bio, city, category_id, image_url, contact_email, years_exp) VALUES (?, ?, ?, ?, ?, ?, ?)",
#         (data.name, data.bio, data.city, data.category_id, data.image_url, data.contact_email, data.years_exp),
#     )
#     new_id = cursor.lastrowid
#     conn.commit()
#     conn.close()
#     return get_master(new_id)


# @app.put("/masters/{master_id}", response_model=MasterOut)
# def update_master(master_id: int, data: MasterCreate):
#     conn = database.get_connection()
#     conn.execute(
#         "UPDATE masters SET name=?, bio=?, city=?, category_id=?, image_url=?, contact_email=?, years_exp=? WHERE id=?",
#         (data.name, data.bio, data.city, data.category_id, data.image_url, data.contact_email, data.years_exp, master_id),
#     )
#     conn.commit()
#     conn.close()
#     return get_master(master_id)


# @app.delete("/masters/{master_id}", status_code=204)
# def delete_master(master_id: int):
#     conn = database.get_connection()
#     conn.execute("DELETE FROM masters WHERE id = ?", (master_id,))
#     conn.commit()
#     conn.close()


# @app.post("/sessions", response_model=SessionOut, status_code=201)
# def create_session(data: SessionCreate):
#     conn = database.get_connection()
#     cursor = conn.cursor()
#     cursor.execute(
#         "INSERT INTO sessions (master_id, title, description, type, duration_hr, price_range, max_people) VALUES (?, ?, ?, ?, ?, ?, ?)",
#         (data.master_id, data.title, data.description, data.type, data.duration_hr, data.price_range, data.max_people),
#     )
#     new_id = cursor.lastrowid
#     conn.commit()
#     conn.close()
#     return dict(conn.execute("SELECT * FROM sessions WHERE id=?", (new_id,)).fetchone())
