# Kargah — 3-Month Software Engineering Onboarding Plan
> **کارگاه** — A Platform for Discovering Iran's Traditional Artisans & Skill Masters

---

## Quick Reference

| Item | Value |
|---|---|
| Duration | 12 Weeks (3 Months) + 2-week buffer recommended |
| Weekly Hours | 25–30 hours |
| Student Level | Absolute Beginner |
| Target Outcome | Junior-ready developer + clear career path identified |
| Product Status | Demo-ready MVP at end of Month 3 |
| Target Interview Companies | Iranian tech leaders: Snapp, Digikala, Cafe Bazaar, Divar, Tapsi, Balad |

---

## 1. Honest Assessment: Is 3 Months Enough?

**Short answer: Yes — with a 2-week buffer built in.**

Starting from zero code knowledge with 25–30 hours/week, here is what 3 months realistically produces:

- A working, demo-ready web product he built himself
- Foundational understanding of web development (frontend + backend + database)
- Awareness of 6+ engineering career paths
- Git workflow, professional practices, and soft skills
- Enough preparation for **junior/trainee-level interviews** at top Iranian tech companies

**What 3 months will NOT produce:** competitive readiness for senior roles or algorithm-heavy FAANG-style interviews. That requires 12+ months of dedicated practice.

**Recommendation:** Treat this as a **3-month core program + 2 bonus weeks of interview polish**. If he is consistent, he finishes strong. If he slips 1–2 weeks, the buffer absorbs it without panic.

---

## 2. The Product: Kargah (کارگاه)

### Concept

**Kargah** is an online discovery platform that connects people with Iran's traditional artisans, craftspeople, and skill teachers — carpet weavers, pottery makers, calligraphers, miniature artists, metalworkers, woodcarvers — and the workshops where they teach.

Think of it as a directory + portfolio + booking-request platform for Iran's massive but digitally invisible artisan economy.

### Why This Idea

| Criteria | Why Kargah Passes |
|---|---|
| Not overcrowded | No dominant player exists in this exact space in Iran |
| Culturally rich | Deep roots in Iranian identity — carpet, miniature, calligraphy, pottery |
| Technically learnable | No complex payments, no real-time features needed for MVP |
| Expandable | Clear path from directory → booking → payments → video lessons → export |
| Interviewable | Student can explain it, demo it, and discuss its architecture clearly |
| Yours to own | Simple enough to build solo; valuable enough to grow into a business |

### MVP Scope (What the Student Builds)

1. Artisan profile pages (name, photo, bio, craft category, city, portfolio images)
2. Browse by category (carpet, pottery, calligraphy, jewelry, etc.)
3. Search by name or city
4. Inquiry/contact form (no real email needed — just a demo form)
5. Admin panel to add/edit/delete artisans
6. Simple authentication (admin login)

### What the Student Does NOT Build (Future Features)

- Online payment integration
- Real booking calendar
- Review/rating system (designed but not fully built)
- Mobile app
- Persian RTL UI polish
- SMS verification

---

## 3. Business Model

> This section is for the student to read, understand, and discuss with the mentor. Understanding WHY a product exists is as important as knowing HOW to build it.

### Problem Statement

Iran has over 200 recognized traditional handicraft categories. Millions of artisans operate invisibly — no online presence, no way for domestic or international buyers to find them. Cultural tourism is growing but tourists cannot discover authentic experiences. Young Iranians are losing access to traditional skill teachers.

### Value Propositions

| User Type | Problem | Kargah's Solution |
|---|---|---|
| Artisans & craftspeople | No digital presence, no new customers | Free profile + portfolio on a searchable platform |
| Cultural tourists | Cannot find authentic craft experiences | Curated discovery with location + category filters |
| Buyers (gifts, decor) | No trusted source for handmade goods | Verified artisan profiles with portfolio proof |
| Learners | Cannot find skill teachers near them | Workshop and teacher listings by city |
| Hotels & tour operators | No curated artisan contacts | B2B directory access |

### Revenue Streams (Phase 2+, not built in this project)

1. **Freemium Listing** — Basic profile is free. Premium (featured placement, analytics, more photos) costs a monthly fee.
2. **Lead Commission** — 5–8% commission on successful inquiries that convert to sales.
3. **Corporate Subscription** — Hotels, travel agencies, and export companies pay for curated artisan directory access.
4. **Promoted Workshops** — Artisans pay to feature their upcoming workshops at the top of listings.
5. **Export Marketplace (long-term)** — Connecting verified artisans with international buyers through a trusted escrow system.

### Market Size Indicators

- Iranian handicraft exports exceeded $500M USD in recent years
- Cultural tourism to Iran brought millions of visitors pre-2020
- Over 3 million Iranians are estimated to be involved in traditional crafts
- No single platform owns this discovery layer yet

---

## 4. Student Profile & Learning Objectives

### Who He Is

- 5th semester computer engineering, Azad University (online)
- Zero coding experience
- ~6 months of hands-on network hardware work (LAN cabling, hospital IT)
- Works best in short focused bursts — not marathon coding sessions
- Needs to find his own path, not be pushed into one

### His Hidden Assets

His network engineering background is a **genuine advantage** in understanding how the internet works. Most developers learn networking abstractly. He has touched the physical layer. Week 1 will connect his existing mental model to software concepts — this is motivating, not remedial.

### Three Learning Objectives

1. **Technical**: Build and understand a full-stack web application from scratch
2. **Career**: Identify which engineering path genuinely interests him (frontend, backend, network/DevOps, data, product, security)
3. **Professional**: Learn how real teams work — Git, tickets, code review, sprints, business thinking

### What "Interview Ready" Means for Him

By Week 12, he should be able to:
- Walk through his Kargah project confidently for 10 minutes
- Explain what a REST API is in plain language
- Write a simple function in Python or JavaScript from scratch
- Explain the difference between frontend and backend
- Describe a database schema he designed
- Use Git to show his commit history as proof of work
- Answer "where do you see yourself in 2 years?" with genuine conviction

---

## 5. The 12-Week Roadmap

### Overview

```
Month 1 — Foundations         Weeks 1–4    "Learning to speak the language"
Month 2 — Building Blocks     Weeks 5–8    "Learning to build things"
Month 3 — Product Sprint      Weeks 9–12   "Building something real"
```

### Month 1: Foundations

**Goal:** Understand how technology works, set up tools, write first code, build first webpage.

---

**Week 1 — The Landscape + Two Superpowers**
*Theme: Understand the world, set up every tool, make the first commit — on Day 1.*

| Day | Topic | Hours |
|---|---|---|
| 1 | How computers work: CPU, RAM, storage, OS. Processes vs threads. Virtual machines. | 3 |
| 1 | **Git Day 1**: install Git, create GitHub account, create Kargah repo, write README, first commit, push to GitHub. Non-negotiable — this happens before anything else. | 2 |
| 2 | How the internet works: IP, DNS, HTTP, HTTPS, TCP/IP — connects to his network experience | 3 |
| 3 | Technology career map: frontend, backend, mobile, DevOps, network, data, security, product | 2 |
| 3 | **AI Tools Day 1**: create accounts on Claude.ai and ChatGPT. Read PROMPT_CHEATSHEET.md. Have 3 AI conversations: "explain CPU", "explain DNS", "explain what programming is". | 2 |
| 4 | Set up workspace: VS Code extensions, WSL, Git config, GitHub SSH key | 3 |
| 5–7 | Research Kargah's domain. Write `docs/problem-statement.md` in the repo. Commit. Ask Claude to review the writing. Commit the improved version. | 7 |

*Path Exposure: Network Engineering (deepens existing knowledge)*
*Soft Skill: Writing clearly, asking smart AI questions, committing daily*
*Git target end of Week 1: 10–15 commits*

---

**Week 2 — Terminal, Git Deep Dive & Linux Basics**
*Theme: Become fluent in the command line. Go deeper than init/add/commit.*

| Day | Topic | Hours |
|---|---|---|
| 1–2 | Terminal deep dive: file system navigation, pipes, environment variables, WSL Linux basics | 6 |
| 3 | Git internals: what a commit really is, branches as pointers, HEAD, git diff | 3 |
| 4 | Git branching workflow: create, switch, merge, delete. Deliberately cause and resolve a merge conflict. | 3 |
| 5 | GitHub: Pull Requests, Issues, README badges. Set up personal GitHub profile README. | 3 |
| 6–7 | Practice: create 5 feature branches in Kargah repo, write small changes, open PRs, review and merge them. Accumulate 20+ commits by end of week. | 5 |

*Path Exposure: DevOps / System Administration / Linux*
*Soft Skill: Documentation, using GitHub Issues for task tracking*
*Git target end of Week 2: 30–40 commits, 3+ PRs merged, 1 merge conflict resolved*

---

**Week 3 — Learning to Think in Code**
*Theme: Python basics*

| Day | Topic | Hours |
|---|---|---|
| 1–2 | Variables, data types (string, int, float, bool), print, input | 6 |
| 3 | Conditions: if / elif / else | 3 |
| 4 | Loops: for, while | 3 |
| 5 | Functions: defining, calling, parameters, return values | 3 |
| 6–7 | Mini project: Command-line artisan directory. User can type a category and see a list of artisans (data stored in a list of dictionaries). | 5 |

*Path Exposure: Software / Backend Development*
*Soft Skill: Breaking a problem into small steps before writing code*

---

**Week 4 — The Web**
*Theme: HTML & CSS — making things visible*

| Day | Topic | Hours |
|---|---|---|
| 1 | What is the web? Browser, server, HTML, CSS, JS roles | 2 |
| 2–3 | HTML: tags, headings, paragraphs, links, images, lists, forms | 6 |
| 4–5 | CSS: selectors, colors, fonts, margins, padding, box model, flexbox basics | 6 |
| 6–7 | Build Kargah's first static page: an artisan profile page in HTML/CSS | 6 |

**End of Month 1 Check-in:** Mentor meeting. Student presents his command-line artisan directory (Python) and his static HTML artisan profile page. First path-interest conversation: "What felt most interesting this month?"

*Path Exposure: Frontend / Client Development*

---

### Month 2: Building Blocks

**Goal:** Learn JavaScript, backend development, databases, and connect them into a working app.

---

**Week 5 — Making Pages Alive**
*Theme: JavaScript basics*

| Day | Topic | Hours |
|---|---|---|
| 1–2 | JS basics: variables, functions, DOM selection | 6 |
| 3–4 | Events: click, submit, input. Changing the page dynamically | 6 |
| 5 | Arrays and objects in JS. JSON format. | 3 |
| 6–7 | Add interactivity to Kargah's artisan page: category filter buttons that show/hide artisans | 5 |

*Path Exposure: Frontend / Client Development*

---

**Week 6 — The Other Side of the Web**
*Theme: Backend & APIs*

| Day | Topic | Hours |
|---|---|---|
| 1 | What is a server? Client-server model. HTTP methods: GET, POST, PUT, DELETE | 3 |
| 2–3 | What is a REST API? JSON responses. Using Postman to test APIs. | 6 |
| 4–5 | FastAPI introduction: create first endpoint, run local server | 6 |
| 6–7 | Build Kargah's first API: GET /artisans returns a list of artisans from Python code | 5 |

*Path Exposure: Backend Development*

---

**Week 7 — Remembering Things**
*Theme: Databases & SQL*

| Day | Topic | Hours |
|---|---|---|
| 1–2 | What is a database? Tables, rows, columns. SQL basics: SELECT, INSERT, UPDATE, DELETE | 6 |
| 3 | SQLite with Python: sqlite3 library. Running queries from code. | 3 |
| 4 | Database design: designing Kargah's schema (artisans, categories, cities tables) | 3 |
| 5 | Relations: foreign keys, JOIN queries | 3 |
| 6–7 | Create Kargah's database. Seed it with 10 sample artisans. Connect it to the FastAPI backend. | 5 |

*Path Exposure: Data Engineering / Database Administration*

---

**Week 8 — Connecting the Dots**
*Theme: Full stack — frontend + backend + database working together*

| Day | Topic | Hours |
|---|---|---|
| 1–2 | Connecting FastAPI to SQLite: real database-backed API endpoints | 6 |
| 3–4 | Frontend calling backend: JavaScript fetch() to get artisans from the API | 6 |
| 5 | Error handling basics: what happens when things go wrong | 3 |
| 6–7 | Build first complete Kargah flow: browse artisans → click one → see profile (all connected) | 5 |

**End of Month 2 Check-in:** Student demos a working (even if rough) full-stack mini-app. Second path-interest conversation: "Backend, frontend, or database — which week did you look forward to most?"

---

### Month 3: Product Sprint

**Goal:** Build, polish, and present the Kargah MVP. Learn professional workflows. Prepare for interviews.

---

**Week 9 — Sprint 1: Core Product**
*Theme: Building Kargah for real, with professional process*

| Day | Task | Hours |
|---|---|---|
| 1 | Introduction to Agile/Scrum: what is a sprint, what is a user story, what is a backlog | 3 |
| 1 | Create GitHub Issues for all Kargah MVP features. Assign to himself. | 2 |
| 2–3 | Build: Artisan listing page (connected to real database, with category filter) | 8 |
| 4–5 | Build: Artisan detail page (full profile, portfolio images) | 8 |
| 6–7 | Build: Search functionality (search by name or city) | 4 |

*Soft Skills: Sprint planning, writing user stories, managing GitHub Issues*

---

**Week 10 — Sprint 2: Admin & Polish**
*Theme: Making it manageable by non-technical users*

| Day | Task | Hours |
|---|---|---|
| 1–2 | Build: Simple admin login (username + password, session-based) | 6 |
| 3–4 | Build: Admin panel — add new artisan, edit existing artisan, delete artisan | 8 |
| 5 | Introduction to Docker: what is containerization, why it matters. Run a simple Docker container. | 4 |
| 6–7 | Code review session with mentor: review each other's code, write comments, suggest improvements | 6 |

*Path Exposure: DevOps / Containerization (awareness level)*
*Soft Skill: Giving and receiving code review*

---

**Week 11 — Working Like a Professional**
*Theme: Processes, soft skills, and understanding the full development world*

| Day | Topic | Hours |
|---|---|---|
| 1 | Git branching strategy: feature branches, pull requests, merge conflicts | 4 |
| 2 | Reading a PRD (Product Requirements Document): analyze a real-world PRD example | 3 |
| 3 | Write a mini-PRD for one new Kargah feature (e.g., "Review System") | 3 |
| 4 | Understanding roles: PM, Designer, Frontend Dev, Backend Dev, QA, DevOps, Data Engineer | 3 |
| 5 | Security basics awareness: SQL injection, authentication, HTTPS, never storing plain passwords | 3 |
| 6–7 | Polish Kargah: fix bugs, improve UI, clean up code, write proper README | 6 |

*Soft Skills: Technical writing, cross-functional thinking, security awareness*

---

**Week 12 — Demo Day & Career Launch**
*Theme: Ship it, present it, get ready for what comes next*

| Day | Task | Hours |
|---|---|---|
| 1–2 | Final Kargah polish and demo preparation | 6 |
| 3 | Create personal GitHub profile README (bio, skills, projects, contact) | 3 |
| 4 | Interview preparation: common CS questions, behavioral questions (STAR method) | 4 |
| 5 | Mock interview with mentor: 30-min technical + 30-min behavioral | 3 |
| 6 | Path reflection session: reviewing all 12 weeks, making a decision on primary path to pursue | 3 |
| 7 | Kargah Demo Day: present the full product to a small audience (mentor + 1–2 others) | 3 |

---

## 6. Career Path Discovery Framework

Throughout the 12 weeks, the student is exposed to 7 distinct engineering paths. At Weeks 4, 8, and 12, he completes a short self-assessment.

### Paths Covered

| Path | When Covered | Depth |
|---|---|---|
| Network Engineering | Week 1 | Deep (has background) |
| System Admin / DevOps | Weeks 2, 10 | Medium |
| Backend Development | Weeks 3, 6, 7, 8, 9 | Deep |
| Frontend / Client Development | Weeks 4, 5, 8, 9 | Deep |
| Database / Data Engineering | Week 7 | Medium |
| Product Management | Week 11 | Awareness |
| Security Engineering | Week 11 | Awareness |

### Weekly Reflection Log (to be filled each Friday)

```
Week: ___
1. What task this week made time disappear? (Flow state)
2. What task made me dread opening the laptop?
3. What did I search for out of curiosity (not because I had to)?
4. Path leaning this week: ___
```

### Final Path Recommendation Process (Week 12)

Review all 12 weekly logs. Count which path appeared most in "flow state" answers. That is the primary path. The mentor validates based on observation.

---

## 7. Tech Stack

### Why These Technologies

Every choice was made for one of two reasons: *easiest to learn* or *most valuable on a resume in Iran's current job market.*

| Technology | Role | Why Chosen |
|---|---|---|
| **Python** | Primary language | Most readable syntax for beginners. Versatile (web, data, automation). High demand in Iran. |
| **FastAPI** | Backend framework | Modern, Python-based, automatic API documentation, excellent for learning REST concepts |
| **SQLite** | Database | Zero installation. File-based. Perfect for learning SQL without server setup. |
| **HTML / CSS / JavaScript** | Frontend | No framework yet — understanding fundamentals first prevents cargo-culting |
| **Git + GitHub** | Version control | Industry standard. His portfolio lives here. |
| **VS Code** | Editor | Free, powerful, best extension ecosystem. Available on Windows. |
| **WSL (Windows Subsystem for Linux)** | Linux environment | Gives Linux terminal experience without dual-booting. Critical for understanding server environments. |
| **Docker Desktop** | Containerization | Awareness-level exposure. Runs on Windows. No extra hardware needed. |
| **Postman** | API testing | Industry-standard tool for testing APIs without writing frontend first |

### What's Intentionally Excluded from Month 1–3

- React / Vue / Angular (learn vanilla JS first)
- Cloud (AWS, Azure, GCP) — no budget, not needed for demo
- Microservices — premature complexity
- Mobile development — too specialized for this phase

---

## 8. Milestones & Success Criteria

### Month 1 Milestone
- [ ] GitHub profile exists with Kargah repository
- [ ] At least 20 commits pushed
- [ ] Can navigate terminal without help
- [ ] Static artisan profile page renders in browser
- [ ] Command-line artisan directory runs in Python

### Month 2 Milestone
- [ ] FastAPI server runs locally and returns JSON
- [ ] SQLite database created with real artisan data
- [ ] Frontend JavaScript fetches data from backend API
- [ ] Full browse → detail flow works end-to-end

### Month 3 Milestone
- [ ] Admin panel with login, add/edit/delete artisans
- [ ] Search and category filter functional
- [ ] GitHub Issues used to track all tasks
- [ ] Code review completed with mentor
- [ ] Kargah demo presented confidently for 10 minutes
- [ ] Personal GitHub README updated

### Interview Readiness Checklist
- [ ] Can explain Kargah's architecture without notes
- [ ] Can write a simple Python function live
- [ ] Understands what GET, POST, PUT, DELETE mean
- [ ] Can draw a simple database schema on a whiteboard
- [ ] Has answered 10 behavioral questions in practice
- [ ] Has decided on a primary career path with reasons

---

## 9. Weekly Schedule Template

Designed for someone who cannot focus for long hours at a stretch.

```
Monday      3–4 hours      New concept (video + reading)
Tuesday     3–4 hours      Practice exercises for Monday's concept
Wednesday   3–4 hours      Apply concept to Kargah
Thursday    2–3 hours      Review, fix bugs, ask mentor questions
Friday      2–3 hours      Weekly reflection log + Git commit cleanup
Weekend     4–6 hours      Free deep work OR rest — student chooses
```

**Rule:** No session longer than 90 minutes without a 20-minute break.
**Rule:** Every week ends with at least one meaningful GitHub commit to Kargah.

---

## 10. Mentor Touchpoints

| When | Format | Duration | Agenda |
|---|---|---|---|
| Week 1, Day 1 | Kickoff meeting | 1 hour | Explain the full plan, answer questions, set expectations |
| End of each week | Async (voice note or message) | 10 min | Student shares what he built, mentor responds with one piece of feedback |
| End of Month 1 | Video call | 45 min | Live demo of Month 1 output, path check-in |
| End of Month 2 | Video call | 45 min | Full-stack demo, course correction if needed |
| Week 10 | Code review session | 1.5 hours | Actual code review of Kargah codebase |
| Week 12 | Mock interview | 1 hour | 30 min technical + 30 min behavioral |
| Week 12 | Demo Day | 30 min | Kargah final presentation |

---

## 11. Rules of the Program

1. **Ship something every week.** Even a broken page is better than no page.
2. **Google is not cheating.** Every professional developer searches constantly. The skill is knowing what to search.
3. **Commit daily.** The GitHub history is his resume. Green squares are proof of work.
4. **Ask before you stay stuck for 30 minutes.** Struggling is good. Being blocked for hours is not.
5. **The university courses come first on exam weeks.** This plan bends for his degree. The degree does not bend for this plan.
6. **No comparison.** This plan is not calibrated to what others his age are doing. It's calibrated to him.

---

*Document version 1.0 — Created May 2026*
*Owner: Mohammad Rezaei*
*Student: [Student Name]*
