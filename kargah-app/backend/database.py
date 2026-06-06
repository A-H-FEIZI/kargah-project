import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "kargah.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            name     TEXT NOT NULL,
            name_fa  TEXT NOT NULL,
            emoji    TEXT DEFAULT '🎨'
        )
    """)

    # Masters (Ustads) — the supply side of the marketplace
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS masters (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            name          TEXT NOT NULL,
            bio           TEXT,
            city          TEXT,
            category_id   INTEGER,
            image_url     TEXT,
            contact_email TEXT,
            years_exp     INTEGER,
            created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    """)

    # Sessions — what each master offers
    # type: 'studio' | 'mobile' | 'commission'
    #   studio     = seeker comes to master's workshop
    #   mobile     = master travels to seeker (سیار)
    #   commission = custom order / commissioned piece
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            master_id   INTEGER NOT NULL,
            title       TEXT NOT NULL,
            description TEXT,
            type        TEXT NOT NULL CHECK(type IN ('studio', 'mobile', 'commission')),
            duration_hr REAL,
            price_range TEXT,
            max_people  INTEGER DEFAULT 1,
            created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (master_id) REFERENCES masters(id)
        )
    """)

    # Booking requests — seekers inquire about a session
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS booking_requests (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id  INTEGER NOT NULL,
            seeker_name TEXT NOT NULL,
            seeker_email TEXT NOT NULL,
            message     TEXT,
            requested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (session_id) REFERENCES sessions(id)
        )
    """)

    # TODO Week 10: add admin_users table for real authentication
    # CREATE TABLE IF NOT EXISTS admin_users (
    #     id            INTEGER PRIMARY KEY AUTOINCREMENT,
    #     username      TEXT NOT NULL UNIQUE,
    #     password_hash TEXT NOT NULL
    # )

    conn.commit()
    conn.close()
