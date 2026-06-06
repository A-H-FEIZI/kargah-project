# Kargah — Setup Guide
> راهنمای راه‌اندازی — Day 1 instructions for the student

---

## What You Need Installed

- Python 3.10+ — [python.org](https://python.org)
- VS Code — [code.visualstudio.com](https://code.visualstudio.com)
- Git — [git-scm.com](https://git-scm.com)

Check versions in terminal:
```bash
python --version
git --version
```

---

## Step 1 — Open the project in VS Code

```
File → Open Folder → kargah-project/kargah-app
```

---

## Step 2 — Set up the Python backend

Open a terminal in VS Code (`Ctrl + `` ` ``).

```bash
cd backend

# Create a virtual environment (do this once)
python -m venv venv

# Activate it (do this every time you open a new terminal)
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies (do this once)
pip install -r requirements.txt

# Create the database and fill it with sample data (do this once)
python seed_data.py

# Start the backend server
uvicorn main:app --reload
```

The API is now running at: **http://127.0.0.1:8000**
Auto-generated docs: **http://127.0.0.1:8000/docs**

---

## Step 3 — Open the frontend

Open a **second terminal** (keep the backend running in the first one).

The simplest way to serve the frontend:

```bash
cd frontend
python -m http.server 5500
```

Then open your browser at: **http://127.0.0.1:5500**

Or install the VS Code extension **"Live Server"** — right-click `index.html` → "Open with Live Server".

---

## Step 4 — Verify everything works

1. Open `http://127.0.0.1:5500` — you should see the artisan listing page
2. Artisan cards should appear (loaded from the API)
3. Category filter and search should work
4. Click an artisan → profile page loads
5. Go to `http://127.0.0.1:5500/admin/login.html`
   - Username: `admin`
   - Password: `kargah2026`
6. Admin dashboard should show the artisan table

---

## Project Structure

```
kargah-app/
├── backend/
│   ├── main.py          ← FastAPI app — all API endpoints
│   ├── database.py      ← SQLite connection and table setup
│   ├── seed_data.py     ← Run once to fill DB with sample data
│   └── requirements.txt ← Python dependencies
│
├── frontend/
│   ├── index.html       ← Artisan listing page
│   ├── artisan.html     ← Single artisan profile page
│   ├── admin/
│   │   ├── login.html   ← Admin login
│   │   ├── dashboard.html ← Admin panel
│   │   └── admin.js     ← Admin panel logic
│   ├── css/
│   │   └── style.css    ← All styles
│   └── js/
│       ├── main.js      ← Listing page logic
│       └── artisan.js   ← Profile page logic
│
├── .gitignore
└── SETUP.md             ← This file
```

---

## Admin Credentials (Demo Only)

| Field | Value |
|---|---|
| Username | `admin` |
| Password | `kargah2026` |

> Week 10 task: replace this with real authentication (hashed passwords stored in the database).

---

## Common Problems

**"uvicorn: command not found"**
→ Make sure your virtual environment is activated (you should see `(venv)` in the terminal).

**Artisans not loading / "Could not load artisans"**
→ Make sure the backend is running (`uvicorn main:app --reload`) before opening the frontend.

**"No module named fastapi"**
→ Run `pip install -r requirements.txt` inside the `backend/` folder with venv activated.

**Database is empty**
→ Run `python seed_data.py` from inside the `backend/` folder.
