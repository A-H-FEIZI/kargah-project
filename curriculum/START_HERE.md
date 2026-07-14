# START HERE — Kargah Project
### Read this file first. Then close it and open WEEKLY_PLAN_EN.md.

---

## What This Project Is

You are going to spend 3 months building **Kargah** — a real web platform that connects Iranian craft masters with people who want to learn from them. By the time you finish, you will have:

- A working web product you built yourself, visible on GitHub
- Enough knowledge to interview for junior developer jobs
- A clear idea of which engineering path you want to follow

You are starting from zero coding knowledge. That is fine. This plan is written exactly for that.

---

## The Only Rule

**Every day you work, you make at least one Git commit.**
Even if you just wrote notes. Even if nothing works yet.
Your commit history is your resume. Start building it today.

---

## File Structure — What Each File Is For

```
kargah-project/
│
├── START_HERE.md              ← You are here. Read once.
│
├── WEEKLY_PLAN_EN.md          ← YOUR MAIN GUIDE. Open this every day.
│                                 Day-by-day tasks for all 12 weeks.
│
├── WEEKLY_PLAN_FA.md          ← Same as above, in Persian.
│
├── PROMPT_CHEATSHEET.md       ← Keep this open in VS Code at all times.
│                                 Copy-paste AI prompts from here when stuck.
│
├── PROMPT_CHEATSHEET_FA.md    ← Same in Persian.
│
├── STUDENT_WEEKLY_LOG.md      ← Fill in every Friday. 10 minutes.
│                                 Tracks which career path interests you.
│
├── INTERVIEW_PREP.md          ← Read during Weeks 11–12 only.
│                                 Technical Q&A and demo script for job interviews.
│
└── kargah-app/                ← The starter code for your product.
    ├── SETUP.md               ← How to run the app locally.
    ├── backend/               ← Python FastAPI server
    └── frontend/              ← HTML, CSS, JavaScript
```

**Files you do NOT need to read:** `PROJECT_PLAN.md`, `RESOURCES.md` — those are for your mentor, not for you.

---

## How to Use These Files Daily

```
Saturday morning:    Open WEEKLY_PLAN_EN.md → find your current week → read Saturday's tasks
While working:       Keep PROMPT_CHEATSHEET.md open in a second VS Code tab
End of every day:    Run: git add . && git commit -m "what you did"
Every Wednesday:     Fill in STUDENT_WEEKLY_LOG.md → commit it
Weeks 11–12:         Add INTERVIEW_PREP.md to your daily reading
```

---

## Before You Do Anything Else — Day 1 Setup

Do these steps right now, in order. Do not skip any.

### Step 1 — Install VS Code (10 minutes)

1. Open your browser → go to **code.visualstudio.com**
2. Click "Download for Windows" → install it (accept all defaults)
3. Open VS Code
4. Press `Ctrl + Shift + X` to open Extensions
5. Search and install these 4 extensions:
   - `Prettier - Code formatter` (by Prettier)
   - `GitLens` (by GitKraken)
   - `Live Server` (by Ritwick Dey)
   - `Python` (by Microsoft)

### Step 2 — Install Git (10 minutes)

1. Go to **git-scm.com** → click "Download for Windows"
2. Install it — accept ALL default settings (do not change anything)
3. After install, open VS Code → press `Ctrl + `` ` `` ` to open the terminal
4. Type: `git --version` and press Enter
5. You should see something like `git version 2.xx.x` — if yes, Git is installed

### Step 3 — Create GitHub Account (10 minutes)

1. Go to **github.com** → click "Sign up"
2. Use your real name in your username if possible (e.g., `ali-rezaei`) — hiring managers see this
3. Verify your email
4. Go back to VS Code terminal and type these two lines (replace with your info):
   ```
   git config --global user.name "Ali Rezaei"
   git config --global user.email "ali@gmail.com"
   ```

### Step 4 — Create AI Tool Accounts (10 minutes)

1. Go to **claude.ai** → sign up (free) — this is your primary AI assistant
2. Go to **chatgpt.com** → sign up (free) — backup assistant
3. Open `PROMPT_CHEATSHEET.md` in VS Code — you'll use this constantly

### Step 5 — Create Your Kargah Repository (20 minutes)

1. On your Desktop, create a new folder called `kargah`
2. Open VS Code → `File → Open Folder` → select the `kargah` folder
3. Open terminal in VS Code (`Ctrl + `` ` ```)
4. Type this exactly:
   ```
   git init
   ```
5. Right-click in the VS Code file panel (left side) → `New File` → name it `README.md`
6. Type this in the file:
   ```markdown
   # Kargah

   A platform connecting traditional Iranian craft masters with people who want to learn from them.

   **Status:** In development — learning project, started [today's date]
   ```
7. Save (`Ctrl + S`)
8. In terminal, type these lines one by one, pressing Enter after each:
   ```
   git add README.md
   git commit -m "init: create Kargah project"
   ```
9. Go to **github.com** → click the `+` button → `New repository`
   - Repository name: `kargah`
   - Description: `Iranian craft master marketplace — learning project`
   - Select `Public`
   - **Do NOT** check "Initialize this repository"
   - Click "Create repository"
10. GitHub will show you a page with commands. Copy and paste the section under **"…or push an existing repository from the command line"** into your VS Code terminal
11. Press Enter after each line
12. Refresh your GitHub page — you should see your README

**You just made your first commit and pushed your first repository. This is the most important step of Day 1.**

---

## Now Open WEEKLY_PLAN_EN.md

Go to Week 1 and follow the tasks in order.
Come back here only if you need to re-read the setup instructions.
