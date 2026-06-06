# Kargah — 12-Week Weekly Plan
### Open this file every day. Find your current week. Do today's tasks in order.

---

## How to use this file

- **Morning**: Read today's tasks before you open anything else.
- **While working**: Keep `PROMPT_CHEATSHEET.md` open in a second VS Code tab.
- **End of every day**: Run `git add . && git commit -m "your message"` — even if nothing works yet.
- **Every Wednesday**: Fill in `STUDENT_WEEKLY_LOG.md` and commit it.

---

# WEEK 1 — How Computers and the Web Actually Work

**Learning goal:** Understand what happens between your keyboard and a website loading.
**Kargah goal:** Have your project folder on GitHub with a working dev environment.

> Day 1 setup (VS Code, Git, GitHub, first commit) is in `START_HERE.md`. Complete that first, then start below.

---

## Saturday — The Machine Under the Code

**What you're learning:** CPU, RAM, storage, processes, threads — the physical reality your code runs on.

**Step 1 — Read (20 min)**

Open your browser. Read this page top to bottom:
`https://cs.fyi/guide/how-does-internet-work`

While you read, open a new file in VS Code: `notes/week1.md`
Write your own one-sentence answer to each question as you find it:
- What is a CPU?
- What is RAM and why does it disappear when you restart?
- What is a process?
- What is a thread, and how is it different from a process?

**Step 2 — Ask Claude (15 min)**

Open claude.ai and paste this prompt:
```
Explain the difference between a process and a thread like I'm someone who knows 
what a computer is but has never written code. Use a cooking analogy. 
Then show me a tiny Python example that creates two threads doing two things at once.
```

Read Claude's answer. Copy the Python example into `notes/week1.md` with a note about what it does.

**Step 3 — Run it (15 min)**

Open VS Code terminal (`Ctrl + backtick`). Make sure you're in your kargah folder.

Create a file `experiments/threads_demo.py`:
```python
import threading
import time

def task(name, seconds):
    print(f"{name} started")
    time.sleep(seconds)
    print(f"{name} finished after {seconds}s")

t1 = threading.Thread(target=task, args=("Task A", 2))
t2 = threading.Thread(target=task, args=("Task B", 1))

t1.start()
t2.start()

t1.join()
t2.join()

print("Both done")
```

Run it: `python experiments/threads_demo.py`

Notice: Task B finishes before Task A even though you started A first. That is threads.

**Step 4 — Git commit**
```
git add .
git commit -m "week1-mon: add thread demo and notes"
```

---

## Sunday — How the Web Works

**What you're learning:** What actually happens when you type a URL and press Enter.

**Step 1 — Watch (20 min)**

Search YouTube for: `"DNS explained in 5 minutes"` — watch the first result from ByteByteGo or similar.

Then read this short page: `https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview`
(You don't need to read every detail — just the first 4 sections.)

**Step 2 — Map it in your notes**

In `notes/week1.md`, write out this sequence in your own words:
```
You type: kargah.ir
→ Your computer asks [?] for the IP address
→ [?] responds with [?]
→ Your browser sends a [?] request to [?]
→ The server responds with [?]
→ Your browser renders [?]
```

Fill in each [?]. Use Claude if you're stuck:
```
I'm a beginner. Walk me through exactly what happens when I type a URL and press Enter — 
from DNS lookup to the page appearing on screen. Use simple language. 
Number each step.
```

**Step 3 — Inspect a real request (15 min)**

Open Chrome or Firefox. Go to any website (e.g., github.com).
Press F12 → click the "Network" tab → refresh the page.

You'll see a list of requests. Click the first one (the main HTML page).
Look at: Status, Method, Request Headers, Response Headers.

In your notes, write: what is the status code? What does it mean?

**Step 4 — Git commit**
```
git add .
git commit -m "week1-tue: add web request notes and DNS explanation"
```

---

## Monday — HTTP, TCP, and Protocols

**What you're learning:** The difference between HTTP, HTTPS, TCP, UDP — and why it matters.

**Step 1 — Read + Ask (25 min)**

Read: `https://roadmap.sh/guides/http-basics` (first half only — up to "HTTP Methods")

Then ask Claude:
```
Explain the difference between TCP and UDP using a real-world analogy. 
Then explain why HTTP uses TCP and not UDP. 
Keep it simple — I just started learning.
```

Add the key points to `notes/week1.md`.

**Step 2 — HTTP methods hands-on (20 min)**

You're going to use `curl` — a tool that sends HTTP requests from your terminal.

In VS Code terminal, type:
```bash
curl -v https://httpbin.org/get
```

This sends a GET request and shows you the full response. Look for:
- The status line (HTTP/1.1 200 OK)
- Response headers
- The JSON body

Now try:
```bash
curl -X POST https://httpbin.org/post -H "Content-Type: application/json" -d '{"name": "Ali"}'
```

Notice how a POST sends data, while GET just requests data.

In your notes: what are GET, POST, PUT, DELETE used for in a one-sentence each summary?

**Step 3 — Git commit**
```
git add .
git commit -m "week1-wed: HTTP methods notes and curl experiments"
```

---

## Tuesday — Networks, Proxies, VPNs

**What you're learning:** IP addresses, firewalls, proxies, reverse proxies, VPNs, CDNs — you've heard these words. Now you'll know what they actually do.

**Step 1 — Ask Claude (20 min)**

Paste this prompt:
```
I have a network engineering background. Explain these networking concepts 
from a software developer's perspective — how they affect the apps I'll build:
1. Proxy vs Reverse Proxy
2. VPN — what it actually does technically
3. Firewall — what a software developer should configure
4. CDN — what it does and when to use it
5. Load balancer — simple explanation

For each one, give a one-sentence "why a developer cares about this."
```

Read Claude's answer carefully. Add key points to `notes/week1.md`.

**Step 2 — Connect to Kargah**

In `notes/week1.md`, answer these with what you just learned:
- When Kargah launches and gets 10,000 users at once — which of these concepts would we need?
- Why would Kargah need HTTPS and not just HTTP?
- If a user in Iran has a proxy, does that change how Kargah serves them?

**Step 3 — Git commit**
```
git add .
git commit -m "week1-thu: network concepts notes - proxy CDN VPN"
```

---

## Wednesday — Review + Weekly Log

**Step 1 — Self-test (20 min)**

Ask Claude:
```
Quiz me on these topics — one question at a time. Wait for my answer before asking the next.
After each answer, tell me what I got right and what I missed.

Topics: process vs thread, how DNS works, difference between HTTP and HTTPS, 
what a proxy does, what a CDN does, TCP vs UDP.
```

Answer each question out loud or in text. Don't look at your notes while answering.

**Step 2 — Fill in weekly log**

Open `STUDENT_WEEKLY_LOG.md`. Fill in Week 1's section honestly.

**Step 3 — Git commit**
```
git add .
git commit -m "week1-fri: weekly log + review quiz"
git push
```

**Week 1 checklist:**
- [ ] `notes/week1.md` exists with your own explanations
- [ ] `experiments/threads_demo.py` exists and you ran it
- [ ] You know what happens when you type a URL (DNS → TCP → HTTP → HTML)
- [ ] You can explain process vs thread in plain words
- [ ] At least 5 commits pushed to GitHub

---

# WEEK 2 — Git Like a Professional + Python Foundations

**Learning goal:** Use Git the way real developers use it. Write your first Python functions.
**Kargah goal:** Kargah repository is structured correctly, with branches. First Python script runs.

---

## Saturday — Git: The Real Way

**What you're learning:** Staging, commits, branches, merging, pull requests.

**Step 1 — Read (20 min)**

Go to: `https://learngitbranching.js.org/`

Complete: **Introduction Sequence** levels 1–4 (interactive — you type real git commands in the browser).

These levels cover: commit, branch, checkout, merge. Do them in order.

**Step 2 — Practice in your real project (20 min)**

In your kargah folder terminal:
```bash
# Check where you are
git status
git log --oneline

# Create a branch for your notes
git checkout -b feature/week2-practice

# Create a file
# (create notes/week2.md in VS Code, write "Week 2 notes" in it)

git add notes/week2.md
git commit -m "week2: add notes file"

# Go back to main
git checkout main

# Merge your branch in
git merge feature/week2-practice

# Push to GitHub
git push
```

Check GitHub — you should see your new file there.

**Step 3 — Ask Claude to explain what you just did**
```
I just ran these git commands: checkout -b, add, commit, checkout main, merge.
Explain what each one did to my repository's internal state. 
What is the "staging area" and why does it exist?
```

Add your understanding to `notes/week2.md`.

**Step 4 — Git commit**
```
git add .
git commit -m "week2-mon: git branching practice"
```

---

## Sunday — Python: Variables, Functions, Lists, Dicts

**What you're learning:** The building blocks you'll use every day in the Kargah backend.

**Step 1 — Read + Try (30 min)**

Go to: `https://docs.python.org/3/tutorial/introduction.html`

Read sections 3.1 (Numbers) and 3.1.2 (Strings) — just read, don't get stuck.

Then create `experiments/python_basics.py` and type these by hand (do NOT copy-paste — typing builds muscle memory):

```python
# Variables
name = "Kargah"
version = 1
is_live = False

print(name, version, is_live)

# Lists
masters = ["Hossein Kalhor", "Zahra Shirazi", "Ali Ebrahimi"]
print(masters[0])           # First item
print(len(masters))         # How many
masters.append("Sara Nazari")
print(masters)

# Dictionaries
master = {
    "name": "Hossein Kalhor",
    "city": "Tehran",
    "craft": "Carpet Weaving",
    "years_exp": 15
}
print(master["name"])
print(master.get("rating", "Not rated yet"))  # .get() with a default

# Loops
for m in masters:
    print(f"Master: {m}")

for key, value in master.items():
    print(f"{key}: {value}")
```

Run it: `python experiments/python_basics.py`

**Step 2 — Functions (20 min)**

Add this to the same file:

```python
# Functions
def greet_master(name, city):
    return f"Welcome, {name} from {city}!"

message = greet_master("Hossein", "Tehran")
print(message)

# Function with a list
def filter_by_city(masters_list, city):
    result = []
    for master in masters_list:
        if master["city"] == city:
            result.append(master)
    return result

all_masters = [
    {"name": "Hossein", "city": "Tehran"},
    {"name": "Zahra", "city": "Isfahan"},
    {"name": "Ali", "city": "Tehran"},
]

tehran_masters = filter_by_city(all_masters, "Tehran")
print(tehran_masters)
```

Run it. If you get an error, paste the full error + your code into Claude using the Debugger template from `PROMPT_CHEATSHEET.md`.

**Step 3 — Git commit**
```
git add .
git commit -m "week2-tue: python basics - variables functions lists dicts"
```

---

## Monday — Python: Classes and Error Handling

**What you're learning:** Object-oriented basics + how to handle things going wrong.

**Step 1 — Classes (25 min)**

Create `experiments/python_classes.py`:

```python
class Master:
    def __init__(self, name, city, craft):
        self.name = name
        self.city = city
        self.craft = craft
        self.sessions = []

    def add_session(self, session_type, price):
        self.sessions.append({"type": session_type, "price": price})

    def describe(self):
        return f"{self.name} — {self.craft} master from {self.city}"

    def __repr__(self):
        return f"Master({self.name})"


# Create instances
hossein = Master("Hossein Kalhor", "Tehran", "Carpet Weaving")
zahra = Master("Zahra Shirazi", "Isfahan", "Miniature Painting")

hossein.add_session("studio", "500,000 tomans")
hossein.add_session("mobile", "800,000 tomans")

print(hossein.describe())
print(hossein.sessions)

masters = [hossein, zahra]
for m in masters:
    print(m)
```

Run it. Ask Claude if any part is unclear:
```
I'm a Python beginner. Explain what __init__ and self do in a class. 
Use a real-world analogy, not a technical definition.
```

**Step 2 — Error Handling (20 min)**

Add to the same file:

```python
# Without error handling — this crashes
# data = {"name": "Ali"}
# print(data["city"])  # KeyError!

# With error handling
def get_city(master_dict):
    try:
        return master_dict["city"]
    except KeyError:
        return "City not provided"

print(get_city({"name": "Ali"}))         # "City not provided"
print(get_city({"name": "Ali", "city": "Tehran"}))  # "Tehran"
```

**Step 3 — Git commit**
```
git add .
git commit -m "week2-wed: python classes and error handling"
```

---

## Tuesday — Python: Files and JSON

**What you're learning:** Reading and writing files, working with JSON — the format APIs use.

**Step 1 — JSON practice (20 min)**

Create `experiments/json_practice.py`:

```python
import json

# Python dict → JSON string
master = {
    "name": "Hossein Kalhor",
    "city": "Tehran",
    "sessions": ["studio", "mobile"]
}

json_string = json.dumps(master, ensure_ascii=False, indent=2)
print(json_string)
print(type(json_string))  # str

# JSON string → Python dict
parsed = json.loads(json_string)
print(parsed["city"])  # Tehran
print(type(parsed))    # dict

# Write to file
with open("experiments/master_data.json", "w", encoding="utf-8") as f:
    json.dump(master, f, ensure_ascii=False, indent=2)

# Read from file
with open("experiments/master_data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded["name"])
```

Run it. Check that `master_data.json` was created in your experiments folder.

**Step 2 — Connect to Kargah**

In `notes/week2.md`, answer: Why does Kargah's API need to return JSON? What would it look like for one master?

**Step 3 — Git commit**
```
git add .
git commit -m "week2-thu: python files and JSON practice"
```

---

## Wednesday — Review + Git Push Week

**Step 1 — Challenge yourself (20 min)**

Without looking at your notes, write a Python function from scratch in a new file `experiments/challenge_week2.py`:

```
Write a function called search_masters(masters_list, city, craft).
It takes a list of master dicts and returns only those matching the city AND craft.
If city is None, match any city.
If craft is None, match any craft.
Test it with at least 4 masters (make them up).
```

If you get stuck, use the Rubber Duck prompt from `PROMPT_CHEATSHEET.md` — but try for 10 minutes first.

**Step 2 — Weekly log + Push**
```
git add .
git commit -m "week2-fri: challenge and weekly log"
git push
```

**Week 2 checklist:**
- [ ] You completed learngitbranching.js.org Introduction levels 1–4
- [ ] You created and merged a branch in your real repo
- [ ] You can write Python functions, classes, and handle errors
- [ ] You understand JSON and can read/write it
- [ ] At least 8 commits total on GitHub

---

# WEEK 3 — Python Deep Dive + Your First API Call

**Learning goal:** Write Python that fetches real data from the internet and processes it.
**Kargah goal:** Python script that talks to an API and returns formatted data.

---

## Saturday — Python: List Comprehensions and Sorting

**What you're learning:** The Pythonic way to work with data — shorter, faster, cleaner.

**Step 1 — Practice (30 min)**

Create `experiments/python_intermediate.py`:

```python
masters = [
    {"name": "Hossein", "city": "Tehran", "years_exp": 15, "price": 500000},
    {"name": "Zahra", "city": "Isfahan", "years_exp": 8, "price": 350000},
    {"name": "Ali", "city": "Tehran", "years_exp": 20, "price": 750000},
    {"name": "Sara", "city": "Shiraz", "years_exp": 5, "price": 250000},
    {"name": "Reza", "city": "Tehran", "years_exp": 12, "price": 600000},
]

# List comprehension — same as a for loop but shorter
names = [m["name"] for m in masters]
print(names)

# With filter
tehran_masters = [m for m in masters if m["city"] == "Tehran"]
print(tehran_masters)

# Sort by price (ascending)
by_price = sorted(masters, key=lambda m: m["price"])
for m in by_price:
    print(f"{m['name']}: {m['price']:,} tomans")

# Sort by experience (descending)
by_exp = sorted(masters, key=lambda m: m["years_exp"], reverse=True)
print([m["name"] for m in by_exp])

# Min and Max
cheapest = min(masters, key=lambda m: m["price"])
most_exp = max(masters, key=lambda m: m["years_exp"])
print(f"Cheapest: {cheapest['name']}")
print(f"Most experienced: {most_exp['name']}")
```

Run it. If `lambda` looks confusing, ask Claude:
```
Explain Python lambda functions using a simple real-world example. 
I already understand regular functions with def. 
How are lambdas different and when should I use them?
```

**Step 2 — Git commit**
```
git add .
git commit -m "week3-mon: list comprehensions and sorting"
```

---

## Sunday — HTTP Requests from Python

**What you're learning:** How to fetch data from an API using Python's `requests` library.

**Step 1 — Install requests**

In your terminal:
```bash
pip install requests
```

**Step 2 — Fetch real data (30 min)**

Create `experiments/fetch_practice.py`:

```python
import requests

# GET request — simplest form
response = requests.get("https://httpbin.org/json")
print(response.status_code)       # 200
print(response.json())            # Python dict

# GET with parameters (like ?city=Tehran&craft=weaving)
params = {"name": "Ali", "city": "Tehran"}
response = requests.get("https://httpbin.org/get", params=params)
data = response.json()
print(data["args"])   # Shows your params came through

# POST with JSON body
payload = {
    "seeker_name": "Ali Rezaei",
    "message": "I want to book a session"
}
response = requests.post(
    "https://httpbin.org/post",
    json=payload
)
data = response.json()
print(data["json"])   # Your payload echoed back

# Error handling
try:
    response = requests.get("https://httpbin.org/status/404")
    response.raise_for_status()   # Raises exception for 4xx/5xx
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
```

Run it. Read each print output carefully. In `notes/week3.md`, write: what is `response.status_code` and why do we check it?

**Step 3 — Git commit**
```
git add .
git commit -m "week3-tue: http requests with Python requests library"
```

---

## Monday — Build Your First Mini-API Client

**What you're learning:** Combining everything into a real script that could power part of Kargah.

**Step 1 — Build it (40 min)**

Create `experiments/kargah_api_client.py`:

```python
"""
Simulates what Kargah's frontend will do:
fetch masters from our API and display them nicely.
"""
import requests

BASE_URL = "https://httpbin.org"  # placeholder until our real API is up

def fetch_masters(city=None, craft=None):
    """Fetch masters with optional filters."""
    params = {}
    if city:
        params["city"] = city
    if craft:
        params["craft"] = craft

    response = requests.get(f"{BASE_URL}/get", params=params)
    
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return []
    
    # In reality this would return real master data
    # For now we just return the echoed params to prove it works
    return response.json()["args"]

def display_masters(masters_data):
    """Display masters in a readable format."""
    if not masters_data:
        print("No masters found.")
        return
    
    print("\n--- Search Results ---")
    for key, value in masters_data.items():
        print(f"  {key}: {value}")
    print("----------------------\n")

# Main program
print("Searching for masters in Tehran...")
results = fetch_masters(city="Tehran")
display_masters(results)

print("Searching for pottery masters...")
results = fetch_masters(craft="pottery")
display_masters(results)
```

Run it. Read the output. Then in `notes/week3.md`, write: in Week 6, what will we change `BASE_URL` to?

**Step 2 — Git commit**
```
git add .
git commit -m "week3-wed: kargah API client prototype"
```

---

## Tuesday — Big-O and Algorithms Basics

**What you're learning:** Why some code is fast and some code is slow — and how to talk about it.

**Step 1 — Read (20 min)**

Go to: `https://www.freecodecamp.org/news/big-o-notation-why-it-matters-and-why-it-doesnt-1674cfa8a23c/`

Read just the first half — up through O(n log n). Skip the math. Focus on the shapes of the graphs.

**Step 2 — Ask Claude (15 min)**
```
Explain Big O notation to a developer who just started coding.
Use a grocery store analogy.
Then show Python examples of O(1), O(n), O(n²) operations.
Show why the O(n²) one would be terrible if we had 10,000 masters on Kargah.
```

**Step 3 — Practice (20 min)**

Create `experiments/bigO_practice.py`:

```python
masters = [{"name": f"Master {i}", "city": "Tehran"} for i in range(1000)]

# O(1) — constant time
def get_first_master(masters_list):
    return masters_list[0]  # Always one operation, no matter the list size

# O(n) — linear time  
def find_master_by_name(masters_list, name):
    for master in masters_list:    # Could check every item
        if master["name"] == name:
            return master
    return None

# O(n²) — quadratic time — BAD for large lists
def find_duplicates_slow(masters_list):
    duplicates = []
    for i in range(len(masters_list)):          # n iterations
        for j in range(len(masters_list)):      # n iterations for EACH i
            if i != j and masters_list[i]["name"] == masters_list[j]["name"]:
                duplicates.append(masters_list[i])
    return duplicates

# O(n) alternative — using a dict
def find_duplicates_fast(masters_list):
    seen = {}
    duplicates = []
    for master in masters_list:               # n iterations, once
        name = master["name"]
        if name in seen:
            duplicates.append(master)
        seen[name] = True
    return duplicates

import time

start = time.time()
find_duplicates_slow(masters[:200])  # only 200 so it doesn't take too long
print(f"Slow version: {time.time() - start:.4f}s")

start = time.time()
find_duplicates_fast(masters)
print(f"Fast version: {time.time() - start:.4f}s")
```

Run it. The difference will be clear.

**Step 4 — Git commit**
```
git add .
git commit -m "week3-thu: big-O notation and algorithm comparison"
```

---

## Wednesday — Data Structures

**What you're learning:** Arrays, hash maps, stacks, queues, trees — when to use each one.

**Step 1 — Ask Claude (20 min)**
```
Explain these data structures with a real-world analogy for each:
1. Array / List
2. Hash Map / Dictionary
3. Stack (LIFO)
4. Queue (FIFO)
5. Binary Tree

Then for each one, give me one concrete example of where Kargah (a marketplace 
for Iranian craft masters) would use it.
```

**Step 2 — Quick demo**

Add to `experiments/bigO_practice.py`:

```python
from collections import deque

# Stack — like a stack of plates (Last In, First Out)
booking_undo_stack = []
booking_undo_stack.append("Book session #1")
booking_undo_stack.append("Book session #2")
print(booking_undo_stack.pop())  # "Book session #2" — last in, first out

# Queue — like a waiting list (First In, First Out)
booking_queue = deque()
booking_queue.append("Ali")
booking_queue.append("Sara")
booking_queue.append("Reza")
print(booking_queue.popleft())  # "Ali" — first in, first out

# Hash map (dict) — instant lookup by key
master_index = {
    "hossein-kalhor": {"city": "Tehran", "craft": "Carpet"},
    "zahra-shirazi": {"city": "Isfahan", "craft": "Miniature"},
}
print(master_index["zahra-shirazi"])  # O(1) lookup
```

**Step 3 — Weekly log + push**
```
git add .
git commit -m "week3-fri: data structures demo and weekly log"
git push
```

**Week 3 checklist:**
- [ ] You can write list comprehensions and sort lists of dicts
- [ ] You can make GET and POST requests from Python
- [ ] You understand O(1), O(n), O(n²) and can give examples
- [ ] You can explain when to use a list vs dict vs queue
- [ ] At least 12 commits on GitHub

---

# WEEK 4 — HTML + CSS: Building Kargah's Faces

**Learning goal:** Write HTML and CSS that produces a real-looking web page.
**Kargah goal:** Master listing page (`index.html`) built and styled — looks like a real product.

---

## Saturday — HTML: Structure First

**What you're learning:** HTML is not programming — it's structure. Every tag has a purpose.

**Step 1 — Read (15 min)**

Go to: `https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started`

Read just the first two sections: "What is HTML?" and "Anatomy of an HTML element."

**Step 2 — Open the starter HTML**

In VS Code, open `kargah-app/frontend/index.html`.

Read through it top to bottom. In `notes/week4.md`, answer:
- What does `<head>` contain? What does `<body>` contain?
- What is `<div class="master-card">`? What does the `class` attribute do?
- Find the `<link>` tag. What does it do?

**Step 3 — Modify it**

In `index.html`, find the hardcoded master cards (if any exist in the HTML). 
If the page loads from JavaScript, look at `js/main.js` instead.

For now, add a `<header>` section at the top of `<body>` that doesn't exist yet:
```html
<header class="site-header">
  <div class="container">
    <h1 class="logo">کارگاه</h1>
    <p class="tagline">Connect with master craftspeople</p>
  </div>
</header>
```

Save. Open with Live Server (right-click `index.html` → Open with Live Server). See your change.

**Step 4 — Branch for frontend work**
```
git checkout -b feature/week4-frontend
git add .
git commit -m "week4-mon: add site header to index.html"
```

---

## Sunday — CSS: Making It Look Real

**What you're learning:** Box model, flexbox, colors, fonts — the minimum you need to build a real UI.

**Step 1 — Read (20 min)**

Go to: `https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model`

Read "What is the CSS box model?" — just the first page. Pay attention to the diagram showing margin, border, padding, content.

**Step 2 — Open the starter CSS**

Open `kargah-app/frontend/css/style.css`. Read the first 50 lines. Find where:
- Colors are defined (CSS variables starting with `--`)
- The `.master-card` class is defined
- Flexbox is used

Ask Claude:
```
I'm reading CSS for the first time. Explain CSS flexbox with a simple visual analogy.
Then explain what "display: flex", "flex-wrap: wrap", and "gap" do when I'm making 
a grid of cards.
```

**Step 3 — Add a style**

In `style.css`, find the `.site-header` rule (or add it if it's missing):
```css
.site-header {
  background: var(--primary);
  color: white;
  padding: 1.5rem 0;
  text-align: center;
}

.logo {
  font-size: 2rem;
  font-weight: 700;
  margin: 0;
}

.tagline {
  margin: 0.25rem 0 0;
  opacity: 0.85;
  font-size: 1rem;
}
```

Save. Check Live Server — you should see a styled header.

**Step 4 — Git commit**
```
git add .
git commit -m "week4-tue: CSS header styles"
```

---

## Monday — Flexbox Mastery

**What you're learning:** Flexbox is how 90% of modern layouts are built. Learn it properly now.

**Step 1 — Play the game (30 min)**

Go to: `https://flexboxfroggy.com/`

Complete all 24 levels. Don't skip — each one teaches something real.

**Step 2 — Apply to Kargah**

Open `index.html` and `style.css`. Find where master cards are displayed.

Make sure the master card grid uses:
```css
.masters-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  padding: 2rem;
}

.master-card {
  flex: 1 1 300px;    /* grow, shrink, min-width 300px */
  max-width: 400px;
}
```

Check Live Server — resize your browser window. The cards should reflow automatically.

**Step 3 — Git commit**
```
git add .
git commit -m "week4-wed: flexbox grid for master cards"
```

---

## Tuesday — Responsive Design

**What you're learning:** Your site should look good on mobile too — Kargah's users will use phones.

**Step 1 — Ask Claude (15 min)**
```
Explain CSS media queries to a beginner. 
Show me how to make a 3-column card grid collapse to 1 column on mobile.
Keep it minimal — just the CSS I need.
```

**Step 2 — Add responsive CSS**

At the bottom of `style.css`, add:
```css
/* Mobile — screens smaller than 768px */
@media (max-width: 768px) {
  .masters-grid {
    flex-direction: column;
    padding: 1rem;
  }

  .master-card {
    max-width: 100%;
  }

  .site-header {
    padding: 1rem 0;
  }

  .logo {
    font-size: 1.5rem;
  }
}
```

To test: Open Chrome DevTools (F12) → click the phone icon (top left of DevTools) → choose "iPhone SE" from the dropdown. Your page should now look like a mobile layout.

**Step 3 — Git commit**
```
git add .
git commit -m "week4-thu: responsive CSS media queries"
```

---

## Wednesday — Merge, Review, Push

**Step 1 — Merge your feature branch**
```bash
git checkout main
git merge feature/week4-frontend
git push
```

**Step 2 — Look at your GitHub**

Go to github.com → your kargah repo. Your commit history should show clear progress.

**Step 3 — Weekly log**
```
git add .
git commit -m "week4-fri: weekly log"
git push
```

**Week 4 checklist:**
- [ ] `index.html` has a styled header
- [ ] Master cards use flexbox and look good at different screen widths
- [ ] You completed Flexbox Froggy
- [ ] You know what margin, padding, border, and `display: flex` do
- [ ] You used a branch and merged it into main

---

# WEEK 5 — JavaScript: Making Pages Interactive

**Learning goal:** Write JavaScript that reads data and updates the page dynamically.
**Kargah goal:** Master listing page loads real data (from mock JSON) and renders it with JavaScript.

---

## Saturday — JavaScript Basics

**What you're learning:** Variables, functions, DOM manipulation — JavaScript is different from Python.

**Step 1 — Read the differences (15 min)**

Ask Claude:
```
I know Python. Explain these JavaScript concepts in terms of what I already know:
1. let vs const vs var
2. Arrow functions vs function declarations
3. Template literals
4. undefined vs null
5. The === operator (why not ==?)
Show a Python equivalent next to each JavaScript example.
```

**Step 2 — Open `js/main.js`**

Read through the existing JavaScript. In `notes/week5.md`, write:
- How does the file wait for the page to load before running?
- What does `document.getElementById()` do?
- Find where it creates HTML — what method does it use?

**Step 3 — Experiment in the browser console**

Open Chrome → any website → F12 → Console tab.

Type these one by one, pressing Enter after each:
```javascript
let name = "Kargah"
console.log(name)

let masters = ["Hossein", "Zahra", "Ali"]
masters.map(m => m.toUpperCase())

document.title = "Testing JavaScript"
```

Watch what happens. The browser's console is your Python REPL for JavaScript.

**Step 4 — Git commit**
```
git add .
git commit -m "week5-mon: JS basics notes and console experiments"
```

---

## Sunday — The DOM: JavaScript Meets HTML

**What you're learning:** The DOM is how JavaScript reads and changes your HTML.

**Step 1 — Understand the DOM (15 min)**

Read: `https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction`
(Just the "What is the DOM?" section — first two paragraphs.)

**Step 2 — Build a dynamic card creator**

Create `experiments/dom_practice.html`:
```html
<!DOCTYPE html>
<html>
<head>
  <title>DOM Practice</title>
  <style>
    .card { border: 1px solid #ccc; padding: 1rem; margin: 1rem; border-radius: 8px; }
  </style>
</head>
<body>
  <h1>Masters</h1>
  <div id="master-list"></div>

  <script>
    const masters = [
      { name: "Hossein Kalhor", craft: "Carpet Weaving", city: "Tehran" },
      { name: "Zahra Shirazi", craft: "Miniature Painting", city: "Isfahan" },
      { name: "Ali Ebrahimi", craft: "Pottery", city: "Shiraz" },
    ];

    const container = document.getElementById("master-list");

    masters.forEach(master => {
      // Create a div
      const card = document.createElement("div");
      card.className = "card";

      // Set its HTML content
      card.innerHTML = `
        <h2>${master.name}</h2>
        <p><strong>Craft:</strong> ${master.craft}</p>
        <p><strong>City:</strong> ${master.city}</p>
      `;

      // Add it to the page
      container.appendChild(card);
    });
  </script>
</body>
</html>
```

Open with Live Server. You should see 3 cards.

**Step 3 — Git commit**
```
git add .
git commit -m "week5-tue: DOM manipulation practice"
```

---

## Monday — fetch() and Async/Await

**What you're learning:** How JavaScript gets data from an API without reloading the page.

**Step 1 — Read (15 min)**

Ask Claude:
```
Explain JavaScript's event loop and why fetch() is asynchronous — in one paragraph,
using a restaurant ordering analogy. Then show the difference between the callback 
style, .then() style, and async/await style for the same fetch call.
I want to understand async/await specifically.
```

**Step 2 — Practice fetch**

Create `experiments/fetch_practice.html`:
```html
<!DOCTYPE html>
<html>
<head><title>Fetch Practice</title></head>
<body>
  <button id="load-btn">Load Data</button>
  <div id="result"></div>

  <script>
    const button = document.getElementById("load-btn");
    const result = document.getElementById("result");

    button.addEventListener("click", async () => {
      result.textContent = "Loading...";

      try {
        const response = await fetch("https://httpbin.org/json");
        
        if (!response.ok) {
          throw new Error(`HTTP error: ${response.status}`);
        }

        const data = await response.json();
        result.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;

      } catch (error) {
        result.textContent = `Error: ${error.message}`;
      }
    });
  </script>
</body>
</html>
```

Open with Live Server. Click the button. Data should appear without page reload.

**Step 3 — Connect to Kargah's backend (preparation)**

Open `kargah-app/frontend/js/main.js`. Find where it fetches data. Confirm the URL it uses — you'll need this when you start the backend.

**Step 4 — Git commit**
```
git add .
git commit -m "week5-wed: fetch and async/await practice"
```

---

## Tuesday — Events, Forms, Filters

**What you're learning:** User input — buttons, dropdowns, forms — driving page changes.

**Step 1 — Add filtering to the experiment**

Update `experiments/dom_practice.html` to add a filter:

Before the `<script>` tag, add:
```html
<select id="city-filter">
  <option value="">All Cities</option>
  <option value="Tehran">Tehran</option>
  <option value="Isfahan">Isfahan</option>
  <option value="Shiraz">Shiraz</option>
</select>
```

Update the script to filter on change:
```javascript
const filter = document.getElementById("city-filter");

function renderMasters(list) {
  container.innerHTML = "";   // Clear existing
  list.forEach(master => {
    const card = document.createElement("div");
    card.className = "card";
    card.innerHTML = `
      <h2>${master.name}</h2>
      <p>${master.craft} — ${master.city}</p>
    `;
    container.appendChild(card);
  });
}

filter.addEventListener("change", () => {
  const selectedCity = filter.value;
  const filtered = selectedCity
    ? masters.filter(m => m.city === selectedCity)
    : masters;
  renderMasters(filtered);
});

renderMasters(masters);  // Initial render
```

Test it — select a city and watch the list change without a page reload.

**Step 2 — Git commit**
```
git add .
git commit -m "week5-thu: event listeners and filtering"
```

---

## Wednesday — Wire Up Kargah Frontend

**Task (40 min):**

Open `kargah-app/frontend/js/main.js`. 

The starter file fetches from `http://localhost:8000`. Your backend isn't running yet, so use mock data for now.

Find the `fetchMasters()` function (or similar). Add a fallback:
```javascript
async function fetchMasters(filters = {}) {
  try {
    // This will work once the backend is running (Week 6+)
    const params = new URLSearchParams(filters);
    const response = await fetch(`http://localhost:8000/masters?${params}`);
    if (!response.ok) throw new Error("API not available");
    return await response.json();
  } catch (error) {
    console.warn("Backend not running — using mock data");
    return getMockMasters();
  }
}

function getMockMasters() {
  return [
    { id: 1, name: "Hossein Kalhor", craft: "Carpet Weaving", city: "Tehran", years_exp: 15 },
    { id: 2, name: "Zahra Shirazi", craft: "Miniature Painting", city: "Isfahan", years_exp: 8 },
  ];
}
```

Open `index.html` with Live Server. Masters should display using mock data.

**Weekly log + push:**
```
git add .
git commit -m "week5-fri: kargah frontend mock data fallback"
git push
```

**Week 5 checklist:**
- [ ] You can create DOM elements from JavaScript
- [ ] You can use fetch() with async/await and handle errors
- [ ] You understand event listeners
- [ ] Kargah index page shows master cards (even with mock data)
- [ ] At least 18 commits on GitHub

---

# WEEK 6 — FastAPI: Building Kargah's Backend

**Learning goal:** Build a real REST API that returns data from Python.
**Kargah goal:** Backend running locally, serving real data to the frontend.

---

## Saturday — FastAPI Intro

**What you're learning:** What a REST API is, and how FastAPI makes it easy.

**Step 1 — Install (5 min)**
```bash
pip install fastapi uvicorn
```

**Step 2 — Your first endpoint (20 min)**

Create `experiments/first_api.py`:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Kargah API is running"}

@app.get("/masters")
def list_masters():
    return [
        {"id": 1, "name": "Hossein Kalhor", "city": "Tehran"},
        {"id": 2, "name": "Zahra Shirazi", "city": "Isfahan"},
    ]
```

Run it:
```bash
uvicorn experiments.first_api:app --reload
```

Open your browser: `http://localhost:8000/masters`

You should see JSON. Also try: `http://localhost:8000/docs` — FastAPI auto-generates documentation!

**Step 3 — Ask Claude**
```
Explain how FastAPI decorators work. What does @app.get("/masters") actually do?
What is uvicorn and why do I need it to run FastAPI?
```

**Step 4 — Git commit**
```
git add .
git commit -m "week6-mon: first FastAPI endpoints"
```

---

## Sunday — Path Parameters and Query Parameters

**What you're learning:** How APIs accept input — the two main patterns.

**Step 1 — Read (10 min)**

Go to: `https://fastapi.tiangolo.com/tutorial/path-params/`
Then: `https://fastapi.tiangolo.com/tutorial/query-params/`

Read both pages (they're short).

**Step 2 — Add parameters to your API**

Update `experiments/first_api.py`:
```python
from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

masters_db = [
    {"id": 1, "name": "Hossein Kalhor", "city": "Tehran", "craft": "Carpet Weaving"},
    {"id": 2, "name": "Zahra Shirazi", "city": "Isfahan", "craft": "Miniature Painting"},
    {"id": 3, "name": "Ali Ebrahimi", "city": "Tehran", "craft": "Pottery"},
]

@app.get("/masters")
def list_masters(city: Optional[str] = None, craft: Optional[str] = None):
    results = masters_db
    if city:
        results = [m for m in results if m["city"] == city]
    if craft:
        results = [m for m in results if m["craft"] == craft]
    return results

@app.get("/masters/{master_id}")
def get_master(master_id: int):
    for master in masters_db:
        if master["id"] == master_id:
            return master
    return {"error": "Not found"}, 404
```

Test in browser:
- `http://localhost:8000/masters`
- `http://localhost:8000/masters?city=Tehran`
- `http://localhost:8000/masters/2`

**Step 3 — Git commit**
```
git add .
git commit -m "week6-tue: path and query parameters in FastAPI"
```

---

## Monday — Pydantic Models and POST

**What you're learning:** How FastAPI validates data coming in (POST requests).

**Step 1 — Read (10 min)**

Go to: `https://fastapi.tiangolo.com/tutorial/body/`

**Step 2 — Add POST endpoint**

Update `experiments/first_api.py`:
```python
from pydantic import BaseModel, EmailStr

class BookingRequest(BaseModel):
    session_id: int
    seeker_name: str
    seeker_email: str
    message: str = ""   # optional, defaults to empty string

bookings = []   # in-memory storage for now

@app.post("/booking-requests")
def create_booking(booking: BookingRequest):
    new_booking = booking.dict()
    new_booking["id"] = len(bookings) + 1
    bookings.append(new_booking)
    return {"message": "Booking request received", "booking": new_booking}

@app.get("/booking-requests")
def list_bookings():
    return bookings
```

Test with curl:
```bash
curl -X POST http://localhost:8000/booking-requests \
  -H "Content-Type: application/json" \
  -d '{"session_id": 1, "seeker_name": "Ali", "seeker_email": "ali@test.com", "message": "Interested!"}'
```

Then: `http://localhost:8000/booking-requests`

**Step 3 — Git commit**
```
git add .
git commit -m "week6-wed: Pydantic models and POST endpoint"
```

---

## Tuesday — Run the Real Kargah Backend

**Step 1 — Set up the Kargah backend (30 min)**

Open `kargah-app/backend/`. Read `../SETUP.md` for the full instructions.

In your terminal (from the `kargah-app/backend/` folder):
```bash
pip install fastapi uvicorn
python database.py   # Creates the database and tables
python seed_data.py  # Fills with sample masters
uvicorn main:app --reload
```

Open `http://localhost:8000/masters` — you should see real Kargah data.
Open `http://localhost:8000/docs` — explore all the endpoints.

**Step 2 — Test every endpoint**

In `notes/week6.md`, for each of these, write what it returns:
- `GET /masters`
- `GET /masters?city=Tehran`
- `GET /masters/1`
- `GET /masters/1/sessions`
- `GET /sessions`
- `GET /sessions?type=mobile`

Use the browser or curl.

**Step 3 — Git commit**
```
git add .
git commit -m "week6-thu: kargah backend running with seed data"
```

---

## Wednesday — Connect Frontend to Backend

**Step 1 — Remove mock data (20 min)**

In `kargah-app/frontend/js/main.js`, remove the mock data fallback. The real backend is now running.

Make sure the frontend fetches from `http://localhost:8000`.

Open `kargah-app/frontend/index.html` with Live Server. With the backend running in another terminal, the frontend should now show real data.

**Step 2 — CORS check**

If you see an error in the browser console about CORS, open `kargah-app/backend/main.py` and check for this (it should already be there):
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

If missing, add it. Ask Claude what CORS is and why it's needed.

**Step 3 — Weekly log + push**
```
git add .
git commit -m "week6-fri: frontend connected to real backend"
git push
```

**Week 6 checklist:**
- [ ] You can build FastAPI endpoints from scratch
- [ ] You understand path params vs query params
- [ ] You can create a POST endpoint with Pydantic validation
- [ ] Kargah backend is running and returning real data
- [ ] Kargah frontend shows real data from the backend
- [ ] At least 24 commits on GitHub

---

# WEEK 7 — Databases: SQLite and SQL

**Learning goal:** Understand relational databases and write real SQL queries.
**Kargah goal:** Understand every table in `database.py` and write queries that power the backend.

---

## Saturday — What is a Database and Why SQL?

**What you're learning:** Why we don't just store data in Python dicts or JSON files.

**Step 1 — Ask Claude (20 min)**
```
I'm a beginner developer. Explain:
1. Why a production app can't just store data in Python lists (give 3 reasons)
2. What a relational database is — use a spreadsheet analogy
3. What SQL is and why we need a special language for it
4. Why SQLite specifically — when is it good and when is it not enough?
```

Add key points to `notes/week7.md`.

**Step 2 — Explore Kargah's database (20 min)**

In your terminal, from `kargah-app/backend/`:
```bash
python -c "import sqlite3; print(sqlite3.sqlite_version)"
```

Install DB Browser for SQLite (free GUI):
`https://sqlitebrowser.org/dl/`

Open `kargah-app/backend/kargah.db` in DB Browser. 

Look at each table: `categories`, `masters`, `sessions`, `booking_requests`.

In `notes/week7.md`, draw the relationships:
- Which table has a foreign key to `categories`?
- Which table has a foreign key to `masters`?
- What does "foreign key" mean?

**Step 3 — Git commit**
```
git add .
git commit -m "week7-mon: database concepts and schema exploration"
```

---

## Sunday — SQL: SELECT, WHERE, JOIN

**What you're learning:** The most important SQL commands you'll use every day.

**Step 1 — Read (15 min)**

Go to: `https://www.w3schools.com/sql/sql_select.asp`

Read through: SELECT, WHERE, AND/OR, ORDER BY, LIMIT. Try the "Try it" examples on the site.

**Step 2 — Write real queries against Kargah**

Open DB Browser → SQL tab. Run each of these and write what they return in `notes/week7.md`:

```sql
-- Get all masters
SELECT * FROM masters;

-- Get masters from Tehran only
SELECT name, city, years_exp FROM masters WHERE city = 'Tehran';

-- Get the top 3 most experienced masters
SELECT name, years_exp FROM masters ORDER BY years_exp DESC LIMIT 3;

-- Get all studio sessions
SELECT title, price_range FROM sessions WHERE type = 'studio';

-- JOIN: get session title + the master's name
SELECT sessions.title, sessions.type, masters.name AS master_name
FROM sessions
JOIN masters ON sessions.master_id = masters.id;

-- COUNT: how many sessions per master?
SELECT master_id, COUNT(*) AS session_count
FROM sessions
GROUP BY master_id;
```

**Step 3 — Git commit**
```
git add .
git commit -m "week7-tue: SQL SELECT WHERE JOIN queries"
```

---

## Monday — SQL: INSERT, UPDATE, DELETE + Transactions

**What you're learning:** Writing data, not just reading it. And why transactions matter.

**Step 1 — Practice writes**

In DB Browser SQL tab:
```sql
-- INSERT a new booking request
INSERT INTO booking_requests (session_id, seeker_name, seeker_email, message)
VALUES (1, 'Test Seeker', 'test@test.com', 'I want to learn pottery');

-- Verify it was added
SELECT * FROM booking_requests;

-- UPDATE — change the message
UPDATE booking_requests 
SET message = 'Updated: I want to book a studio session'
WHERE seeker_email = 'test@test.com';

-- DELETE the test row
DELETE FROM booking_requests WHERE seeker_email = 'test@test.com';
```

**Step 2 — ACID and Transactions**

Ask Claude:
```
Explain ACID properties (Atomicity, Consistency, Isolation, Durability) to a beginner.
Use a bank transfer analogy.
Then show a Python SQLite example of a transaction that inserts two related rows 
and rolls back if either fails.
```

Add to `notes/week7.md`: why would Kargah need a transaction when creating a booking?

**Step 3 — Git commit**
```
git add .
git commit -m "week7-wed: SQL insert update delete and transactions"
```

---

## Tuesday — Database Normalization and Indexes

**What you're learning:** Why the Kargah schema is designed the way it is.

**Step 1 — Ask Claude (15 min)**
```
Explain database normalization — 1NF, 2NF, 3NF — using a simple example.
I have a table with: booking_id, master_name, master_city, session_title, seeker_name.
Walk me through normalizing it step by step.
Then explain what a database index is and when to add one.
```

**Step 2 — Review Kargah's schema**

Open `kargah-app/backend/database.py`. Read the `CREATE TABLE` statements.

In `notes/week7.md`, answer:
- Is the schema normalized? Which normal form?
- Which columns should have indexes added (hint: columns we filter or join on)?
- Add an index to the database — in DB Browser SQL tab:
  ```sql
  CREATE INDEX idx_masters_city ON masters(city);
  CREATE INDEX idx_sessions_type ON sessions(type);
  ```

**Step 3 — Git commit**
```
git add .
git commit -m "week7-thu: normalization review and indexes"
```

---

## Wednesday — Wire Backend to Real DB

**Step 1 — Read `main.py` (30 min)**

Open `kargah-app/backend/main.py`. Find the endpoint `GET /masters`.

Trace the code: where does it connect to the database? How does it execute the SQL query? How does it return results?

In `notes/week7.md`, write the flow in plain words:
```
Request comes in →
database.py creates a connection →
SQL query runs →
results converted to [?] →
FastAPI returns [?]
```

**Step 2 — Modify a query**

In `main.py`, find the `GET /masters` endpoint. Add sorting by `years_exp` descending as a new optional parameter:

```python
@app.get("/masters")
def list_masters(city: Optional[str] = None, sort_by: Optional[str] = None):
    # existing code...
    if sort_by == "experience":
        query += " ORDER BY years_exp DESC"
    # ...
```

Test: `http://localhost:8000/masters?sort_by=experience`

**Step 3 — Weekly log + push**
```
git add .
git commit -m "week7-fri: backend sort parameter and weekly log"
git push
```

**Week 7 checklist:**
- [ ] You can write SELECT, JOIN, WHERE, GROUP BY queries
- [ ] You understand INSERT, UPDATE, DELETE and transactions
- [ ] You can explain normalization with an example
- [ ] You added an index and understand why
- [ ] At least 30 commits on GitHub

---

# WEEK 8 — Full Stack: Frontend Meets Backend

**Learning goal:** Build features end-to-end — from button click to database and back.
**Kargah goal:** Booking request form works. Sessions page loads and filters. Master profile page complete.

---

## Saturday — The Booking Flow End-to-End

**What you're learning:** Tracing a user action through every layer of the stack.

**Step 1 — Map the flow (20 min)**

In `notes/week8.md`, write the full flow for: "Seeker submits a booking request."

```
1. User fills in the form on [which HTML file?]
2. User clicks "Submit"
3. JavaScript [does what?]
4. fetch() sends a [GET/POST?] request to [which URL?]
5. FastAPI receives it at [which endpoint?]
6. Python does [what validation?]
7. SQL executes: [what query?]
8. Response sent back: [what JSON?]
9. JavaScript [updates the page how?]
```

Look at the actual files to fill this in:
- `frontend/master.html` — the booking form
- `frontend/js/master.js` — the submit handler
- `backend/main.py` — the `POST /booking-requests` endpoint
- `backend/database.py` — the SQL

**Step 2 — Test the full flow**

1. Start the backend: `uvicorn main:app --reload` (in `kargah-app/backend/`)
2. Open `master.html` with Live Server
3. Fill in the form and click Submit
4. Check the browser console for errors
5. Check `http://localhost:8000/booking-requests` — is your booking there?

If it doesn't work, use the Rubber Duck prompt:
```
I'm trying to submit a booking form. The form is in master.html. 
The JavaScript is in master.js. The backend endpoint is POST /booking-requests.
When I click Submit, [describe what happens]. 
I expected [what you expected].
Here is my JavaScript fetch code: [paste it]
What am I missing?
```

**Step 3 — Git commit**
```
git add .
git commit -m "week8-mon: traced booking flow end to end"
```

---

## Sunday — Sessions Page

**What you're learning:** Building a page that filters across multiple dimensions.

**Step 1 — Open `sessions.html` and `js/sessions.js`**

The sessions page should let users filter by: session type (studio/mobile/commission), category, city.

Trace how it currently works. If filtering doesn't work, build it:

In `sessions.js`:
```javascript
let allSessions = [];

async function loadSessions() {
  const response = await fetch("http://localhost:8000/sessions");
  allSessions = await response.json();
  renderSessions(allSessions);
}

function renderSessions(sessions) {
  const container = document.getElementById("sessions-grid");
  container.innerHTML = "";

  if (sessions.length === 0) {
    container.innerHTML = "<p>No sessions found.</p>";
    return;
  }

  sessions.forEach(session => {
    const card = document.createElement("div");
    card.className = "session-card";
    card.innerHTML = `
      <span class="session-type-badge session-type-${session.type}">${session.type}</span>
      <h3>${session.title}</h3>
      <p>${session.description || ""}</p>
      <p><strong>Price:</strong> ${session.price_range}</p>
    `;
    container.appendChild(card);
  });
}

// Filter buttons
document.querySelectorAll(".type-filter").forEach(btn => {
  btn.addEventListener("click", () => {
    const type = btn.dataset.type;
    const filtered = type === "all"
      ? allSessions
      : allSessions.filter(s => s.type === type);
    renderSessions(filtered);
  });
});

loadSessions();
```

**Step 2 — Git commit**
```
git add .
git commit -m "week8-tue: sessions page with type filtering"
```

---

## Monday — Master Profile Page

**What you're learning:** Dynamic pages that show different data based on URL parameters.

**Step 1 — Understand URL parameters in JS**

In `notes/week8.md`, explain: how does `master.html?id=3` pass the master ID to JavaScript?

The answer is:
```javascript
const params = new URLSearchParams(window.location.search);
const masterId = params.get("id");
```

**Step 2 — Build the profile page**

Open `js/master.js`. Make sure it:
1. Reads the `id` from the URL
2. Fetches `GET /masters/{id}` for master details
3. Fetches `GET /masters/{id}/sessions` for their sessions
4. Renders both on the page

If incomplete, add the missing parts. Test by visiting `master.html?id=1`, `master.html?id=2`, etc.

**Step 3 — Git commit**
```
git add .
git commit -m "week8-wed: master profile page with sessions"
```

---

## Tuesday — Error States and Loading States

**What you're learning:** Real apps handle failure. Users should never see a blank page.

**Step 1 — Add loading and error states**

For every `fetch()` call in your frontend, make sure you have:

```javascript
async function loadData() {
  const container = document.getElementById("content");
  
  // Loading state
  container.innerHTML = `<div class="loading">Loading...</div>`;
  
  try {
    const response = await fetch("http://localhost:8000/masters");
    
    if (!response.ok) {
      throw new Error(`Server error: ${response.status}`);
    }
    
    const data = await response.json();
    renderData(data);
    
  } catch (error) {
    // Error state — don't leave the user with a blank page
    container.innerHTML = `
      <div class="error-message">
        <p>Could not load masters. Please try again.</p>
        <button onclick="loadData()">Retry</button>
      </div>
    `;
    console.error(error);
  }
}
```

Apply this pattern to all three pages.

**Step 2 — Test error handling**

Stop your backend. Reload the frontend page. You should see the error message, not a blank page.

**Step 3 — Git commit**
```
git add .
git commit -m "week8-thu: loading and error states for all pages"
```

---

## Wednesday — Security: SQL Injection and XSS

**What you're learning:** Two of the most common ways web apps get attacked.

**Step 1 — Ask Claude (20 min)**
```
Explain SQL injection and XSS (Cross-Site Scripting) to a beginner.
For each one:
1. How does the attack work? (simple example)
2. How does FastAPI/Python protect against it?
3. How does using .innerText instead of .innerHTML protect against XSS?
```

**Step 2 — Audit your code**

Check your frontend JavaScript:
- Every place you use `.innerHTML = someData` — is `someData` from user input or from the API?
- If it's from the API (which you control), it's lower risk — but still use `.textContent` for text that could ever contain user input.

Check your backend:
- Does `main.py` use parameterized queries? Look for `?` placeholders in SQL, not string concatenation.

In `notes/week8.md`, write: is Kargah currently vulnerable to SQL injection? Why or why not?

**Step 3 — Weekly log + push**
```
git add .
git commit -m "week8-fri: security audit and weekly log"
git push
```

**Week 8 checklist:**
- [ ] Booking form submits and data appears in the DB
- [ ] Sessions page filters by type
- [ ] Master profile loads the right master by ID
- [ ] Loading and error states exist on all pages
- [ ] You can explain SQL injection and XSS
- [ ] At least 36 commits on GitHub

---

# WEEK 9 — Product Thinking + Sprint Planning

**Learning goal:** Think like a product manager. Write requirements that engineers can build from.
**Kargah goal:** Admin panel functional. User stories written. Sprint planned.

---

## Saturday — What is a User Story?

**What you're learning:** How product requirements are written so engineers build the right thing.

**Step 1 — Read (15 min)**

Go to: `https://www.atlassian.com/agile/project-management/user-stories`

Read the full page.

**Step 2 — Write Kargah's user stories**

Ask Claude:
```
I'm building Kargah — a marketplace connecting Iranian craft masters with people 
who want to learn from them. Masters can offer three types of sessions:
- Studio: student comes to master's workshop
- Mobile (سیار): master travels to student's location
- Commission: student requests custom handmade work

Write 8 user stories for Kargah — 4 from the Seeker's perspective and 4 from 
the Master's perspective. Use the format: "As a [role], I want to [action] so 
that [benefit]."

Then for each story, add: Acceptance Criteria (3 bullet points of "Given/When/Then" format).
```

Create `notes/week9.md` and paste + edit the output.

**Step 3 — Git commit**
```
git add .
git commit -m "week9-mon: user stories for kargah"
```

---

## Sunday — Sprint Planning

**What you're learning:** How engineers decide what to build in 2-week sprints.

**Step 1 — Ask Claude (15 min)**
```
Explain agile sprint planning to a developer who just started. 
What is a sprint? What is a backlog? What is velocity?
What happens in a sprint planning meeting?
Keep it practical — not theoretical.
```

**Step 2 — Plan your Sprint 1**

In `notes/week9.md`, create a sprint plan for what you'll build in Week 9-10:

```
## Sprint 1 — Weeks 9-10

Goal: Working admin panel that lets a master manage their sessions

User Stories IN this sprint:
- [ ] As an admin, I can log in to a protected dashboard
- [ ] As an admin, I can see all pending booking requests
- [ ] As an admin, I can add a new session for a master

Out of scope (next sprint):
- Payment integration
- Email notifications
- Master registration

Definition of Done:
- Feature works end-to-end
- No console errors
- Committed and pushed
```

**Step 3 — Git commit**
```
git add .
git commit -m "week9-tue: sprint 1 plan"
```

---

## Monday — Admin Panel: Backend

**What you're learning:** Protected routes, admin-only endpoints.

**Step 1 — Review existing admin endpoints**

Open `kargah-app/backend/main.py`. Find the commented-out admin routes (marked with `# TODO Week 9/10`).

Uncomment and implement the master creation endpoint:
```python
@app.post("/admin/masters")
def create_master(master: MasterCreate):
    # Check for admin token (simple version)
    # Real auth comes in Week 11
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO masters (name, bio, city, category_id, contact_email, years_exp) VALUES (?, ?, ?, ?, ?, ?)",
        (master.name, master.bio, master.city, master.category_id, master.contact_email, master.years_exp)
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return {"id": new_id, **master.dict()}
```

Test with curl:
```bash
curl -X POST http://localhost:8000/admin/masters \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Master", "city": "Tehran", "category_id": 1, "years_exp": 5, "contact_email": "test@test.com"}'
```

**Step 2 — Git commit**
```
git add .
git commit -m "week9-wed: admin master creation endpoint"
```

---

## Tuesday + Wednesday — Admin Panel: Frontend

**Step 1 — Open admin dashboard**

Open `kargah-app/frontend/admin/dashboard.html` and `admin/admin.js`.

The admin panel should show:
- All booking requests
- Add Master form
- Add Session form

Implement the booking requests section in `admin.js`:
```javascript
async function loadBookingRequests() {
  const response = await fetch("http://localhost:8000/booking-requests");
  const bookings = await response.json();
  
  const table = document.getElementById("bookings-table");
  table.innerHTML = "";
  
  bookings.forEach(booking => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${booking.id}</td>
      <td>${booking.seeker_name}</td>
      <td>${booking.seeker_email}</td>
      <td>${booking.message}</td>
    `;
    table.appendChild(row);
  });
}

loadBookingRequests();
```

**Step 2 — Test the full admin flow**

1. Open `admin/login.html` (credentials: admin / kargah2026)
2. After login, you should go to `admin/dashboard.html`
3. Booking requests should load
4. Use the "Add Master" form to add a new master
5. Check `http://localhost:8000/masters` — is the new master there?

**Step 3 — Weekly log + push**
```
git add .
git commit -m "week9-fri: admin panel frontend and weekly log"
git push
```

---

## Wednesday — Your First Automated Tests

**What you're learning:** Writing tests that verify your code works — without clicking through the browser every time. This is one of the clearest signals to employers that you write professional code.

**Step 1 — Install pytest (5 min)**
```bash
pip install pytest httpx
```

**Step 2 — Ask Claude (15 min)**
```
Explain pytest to a beginner developer. What is a unit test? What is an integration test?
Why do companies care whether you write tests?
Show me how to test a FastAPI endpoint using pytest and the TestClient.
```

**Step 3 — Write your first tests (30 min)**

Create `kargah-app/backend/test_api.py`:
```python
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_masters_returns_list():
    response = client.get("/masters")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_master_by_id():
    response = client.get("/masters/1")
    assert response.status_code == 200
    master = response.json()
    assert "name" in master
    assert "city" in master

def test_get_masters_filter_by_city():
    response = client.get("/masters?city=Tehran")
    assert response.status_code == 200
    masters = response.json()
    for master in masters:
        assert master["city"] == "Tehran"

def test_create_booking_request():
    payload = {
        "session_id": 1,
        "seeker_name": "Test Seeker",
        "seeker_email": "test@test.com",
        "message": "I want to book"
    }
    response = client.post("/booking-requests", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "booking" in data or "id" in data

def test_get_sessions_returns_list():
    response = client.get("/sessions")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
```

Run them from `kargah-app/backend/`:
```bash
pytest test_api.py -v
```

You should see 5 green PASSED lines. If any fail, use the Debugger prompt from `PROMPT_CHEATSHEET.md`.

**Step 4 — Git commit**
```
git add .
git commit -m "week9-wed: first pytest tests for Kargah API"
```

---

**Week 9 checklist:**
- [ ] You have 8 user stories written with acceptance criteria
- [ ] You have a sprint plan
- [ ] Admin can create masters via the API
- [ ] Admin dashboard shows booking requests
- [ ] `test_api.py` exists with 5 passing tests
- [ ] At least 44 commits on GitHub

---

# WEEK 10 — Docker Awareness + Complete the Product

**Learning goal:** Understand containers. Know when to use them.
**Kargah goal:** All pages working end-to-end. Admin panel complete. Product is demonstrable.

---

## Saturday — What is Docker?

**What you're learning:** Why Docker exists and when you'd use it.

**Step 1 — Ask Claude (25 min)**
```
Explain Docker to a developer who has never used it.
Use a cooking analogy (recipe vs. the actual meal, or a food truck vs. a restaurant).

Explain:
1. What problem does Docker solve?
2. What is an image vs. a container?
3. What is a Dockerfile?
4. Why would I use Docker for Kargah in production?
5. What is docker-compose and when is it useful?
```

**Step 2 — Read the Kargah Dockerfile (if it exists)**

Check if `kargah-app/backend/Dockerfile` exists. If it does, read it and annotate each line in `notes/week10.md`:
```
FROM python:3.11-slim    ← use this base image
WORKDIR /app             ← set the working directory
COPY requirements.txt .  ← copy the requirements first (for caching)
...
```

If it doesn't exist, ask Claude:
```
Write a simple Dockerfile for a Python FastAPI app that:
- Uses Python 3.11
- Installs requirements from requirements.txt
- Exposes port 8000
- Runs with uvicorn
Add a comment on every line explaining what it does.
```

**Step 3 — Git commit**
```
git add .
git commit -m "week10-mon: docker concepts and dockerfile notes"
```

---

## Sunday-Monday — Complete All Pages

**Task:** Go through every page of Kargah and make sure it works completely:

**Checklist per page:**

`index.html` (Master Listing):
- [ ] Masters load from API
- [ ] City filter works
- [ ] Category filter works
- [ ] Each card links to the master's profile page

`sessions.html` (Session Browser):
- [ ] All sessions load
- [ ] Filter by type (studio/mobile/commission) works
- [ ] Each card shows price, duration, type badge

`master.html` (Master Profile):
- [ ] Master name, bio, city, photo show
- [ ] Sessions listed below
- [ ] Booking request form submits correctly
- [ ] Success message appears after submission

`admin/login.html`:
- [ ] Login with admin/kargah2026 works
- [ ] Wrong password shows an error

`admin/dashboard.html`:
- [ ] Booking requests table loads
- [ ] "Add Master" form works
- [ ] "Add Session" form works

Fix anything that doesn't work. Use Claude's Debugger prompt for any errors.

```
git add .
git commit -m "week10-wed: all pages complete and tested"
```

---

## Tuesday — VM vs Container

**What you're learning:** When to use a virtual machine and when to use a container.

**Step 1 — Ask Claude (20 min)**
```
Explain the difference between a Virtual Machine (VM) and a Docker container.
As a developer, when would I choose one over the other?
For Kargah deployed on a server — would I use a VM or a container, and why?
```

**Step 2 — MVC Pattern**

Ask Claude:
```
Explain the MVC (Model-View-Controller) pattern.
Map it to Kargah:
- What is the Model in Kargah?
- What is the View?
- What is the Controller?
Does FastAPI use MVC? What pattern does it use instead?
```

Add to `notes/week10.md`.

**Step 3 — Git commit**
```
git add .
git commit -m "week10-thu: VM vs container and MVC pattern notes"
```

---

## Wednesday — Demo Rehearsal

**Task (45 min):**

You're going to walk through Kargah as if showing it to an investor or employer. Do this out loud (or in writing):

1. Open `index.html` with Live Server (backend running in background)
2. "This is Kargah — a marketplace for Iranian craft masters."
3. Show the master listing page. Filter by city.
4. Click a master. Show their profile.
5. Click "Request Session." Fill in the form. Submit.
6. Open admin dashboard. Show the new booking request appearing.
7. Add a new master via the admin panel.

Write your demo script in `notes/week10.md`. 30 seconds per screen.

**Weekly log + push:**
```
git add .
git commit -m "week10-fri: demo script and weekly log"
git push
```

**Week 10 checklist:**
- [ ] All pages work end-to-end
- [ ] Admin panel is functional
- [ ] You can explain Docker in plain words
- [ ] You can explain MVC and map it to Kargah
- [ ] You have a demo script
- [ ] At least 50 commits on GitHub

---

# WEEK 11 — Security, Passwords, and JWT

**Learning goal:** Understand how authentication and authorization actually work.
**Kargah goal:** Admin login uses real hashed passwords. JWT token protects admin routes.

---

## Saturday — Passwords: Never Store in Plain Text

**What you're learning:** How to store passwords safely.

**Step 1 — Ask Claude (20 min)**
```
Explain to a beginner developer why you should never store passwords in plain text.
What is hashing? What is salting? What is bcrypt?
Show a Python example using the 'bcrypt' library to hash a password and verify it.
```

**Step 2 — Implement it**

Install: `pip install bcrypt`

Create `experiments/password_hashing.py`:
```python
import bcrypt

def hash_password(plain_password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(plain_password.encode(), salt)
    return hashed.decode()

def verify_password(plain_password: str, hashed: str) -> bool:
    return bcrypt.checkpw(plain_password.encode(), hashed.encode())

# Test
password = "kargah2026"
hashed = hash_password(password)
print(f"Hashed: {hashed}")
print(f"Correct password: {verify_password(password, hashed)}")
print(f"Wrong password: {verify_password('wrong', hashed)}")
```

Run it. Notice that the hash is different each time, but verification still works (because of salt).

**Step 3 — Git commit**
```
git add .
git commit -m "week11-mon: password hashing with bcrypt"
```

---

## Sunday — JWT: How Login Tokens Work

**What you're learning:** How APIs stay stateless while knowing who you are.

**Step 1 — Ask Claude (20 min)**
```
Explain JWT (JSON Web Tokens) to a beginner.
How is it different from session cookies?
What are the three parts of a JWT?
Why can't a user fake a JWT without the secret key?
Show a Python example of creating and verifying a JWT using the 'python-jose' library.
```

**Step 2 — Implement basic JWT for Kargah admin**

Install: `pip install python-jose`

In `kargah-app/backend/main.py`, add:
```python
from jose import jwt, JWTError
from datetime import datetime, timedelta

SECRET_KEY = "kargah-dev-secret-change-in-production"
ALGORITHM = "HS256"

def create_token(username: str) -> str:
    expire = datetime.utcnow() + timedelta(hours=8)
    return jwt.encode({"sub": username, "exp": expire}, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except JWTError:
        return None

@app.post("/admin/login")
def admin_login(credentials: dict):
    if credentials.get("username") == "admin" and credentials.get("password") == "kargah2026":
        token = create_token("admin")
        return {"access_token": token, "token_type": "bearer"}
    return {"error": "Invalid credentials"}, 401
```

Test with curl:
```bash
curl -X POST http://localhost:8000/admin/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "kargah2026"}'
```

**Step 3 — Git commit**
```
git add .
git commit -m "week11-tue: JWT login endpoint"
```

---

## Monday-Tuesday — PRD: Product Requirements Document

**What you're learning:** How products are documented before engineers build them.

**Step 1 — Ask Claude (15 min)**
```
What is a PRD (Product Requirements Document)?
What sections does a good PRD have?
Show me a simple template for a small web product.
```

**Step 2 — Write Kargah's PRD**

Create `notes/KARGAH_PRD.md`:

```markdown
# Kargah PRD — v1.0

## Product Summary
One paragraph: what Kargah is, who it's for, and what problem it solves.

## Target Users
- Seeker: [describe]
- Master (Ustad): [describe]

## Core User Flows
1. Seeker browsing and booking
2. Master managing their sessions
3. Admin reviewing requests

## Features — v1.0 (MVP)
| Feature | Priority | Status |
|---------|----------|--------|
| Master listing with filters | P0 | Done |
| Session browsing | P0 | Done |
| Booking request form | P0 | Done |
| Master profile page | P0 | Done |
| Admin dashboard | P1 | Done |

## Out of Scope (v2)
- Payment processing
- Master registration (self-serve)
- Reviews and ratings
- Email notifications

## Success Metrics
- How many booking requests submitted per week?
- How many masters listed?
- What is the conversion rate: visitors → booking requests?
```

Fill in all the blanks in your own words.

**Step 3 — Git commit**
```
git add .
git commit -m "week11-wed-thu: kargah PRD draft"
```

---

## Wednesday — Security Audit

**Task (40 min):**

Go through this checklist for Kargah. For each item, note: Secure / Needs fix.

```
Backend:
[ ] Are all SQL queries parameterized? (no string concatenation with user input)
[ ] Is the admin password stored in code? (it is — note this as a v2 fix)
[ ] Are error messages leaking internal details to the user?
[ ] Is there any endpoint that can delete all data without authentication?

Frontend:
[ ] Is any user input rendered with innerHTML? (XSS risk)
[ ] Is the JWT token stored in localStorage? (risk — note as known limitation)
[ ] Are there any hardcoded credentials visible in source? (admin.js check)
```

For each "Needs fix" item, write in `notes/week11.md` what the v2 fix would be.

**Weekly log + push:**
```
git add .
git commit -m "week11-fri: security audit and weekly log"
git push
```

---

# WEEK 12 — Polish, Interview Prep, and Demo Day

**Learning goal:** Present what you built clearly and confidently.
**Kargah goal:** GitHub looks clean. Demo is smooth. You can answer technical questions about your own code.

---

## Saturday — README and GitHub Polish

**Task:**

Open `kargah-app/README.md` (or create it). Write a README that a recruiter would look at:

```markdown
# Kargah — Iranian Craft Masters Marketplace

A two-sided marketplace connecting traditional Iranian craft masters 
(ustads) with people who want to learn from them.

**Live demo:** [your GitHub Pages link if deployed]
**Built in:** 3 months, learning from zero

## Tech Stack
- Backend: Python + FastAPI + SQLite
- Frontend: HTML + CSS + Vanilla JavaScript
- Auth: JWT tokens

## Features
- Master listing with city/craft filters
- Three session types: Studio, Mobile (سیار), Commission
- Booking request form
- Admin dashboard for managing masters and bookings

## Run Locally
[exact setup steps]
```

Also: Go to your GitHub repo → Settings → Social preview → add a screenshot.

**Git commit:**
```
git add .
git commit -m "week12-mon: polish README and GitHub"
```

---

## Sunday — Read `INTERVIEW_PREP.md`

Open `INTERVIEW_PREP.md`. Read all sections.

Ask Claude to quiz you:
```
Quiz me on junior developer interview questions — one at a time.
Cover: REST APIs, SQL, JavaScript async, Git, HTTP, Python basics, 
databases, security basics.
Wait for my answer. Tell me what I got right and what I missed.
Give a model answer I can learn from.
Then ask the next question.
```

Do 10 questions. Take notes in `notes/week12.md`.

**Git commit:**
```
git add .
git commit -m "week12-tue: interview prep notes"
```

---

## Monday — Deploy Kargah Live

**What you're doing:** Putting Kargah on the internet so anyone (including interviewers) can open it without needing to run anything locally. A live URL on your resume is significantly more impressive than "run it on localhost."

**Step 1 — Create a `requirements.txt` (5 min)**

From `kargah-app/backend/`:
```bash
pip freeze > requirements.txt
```

Check that `fastapi`, `uvicorn`, `python-jose`, and `bcrypt` are in the file.

**Step 2 — Deploy to Render (free, no credit card) (30 min)**

1. Go to `render.com` → Sign up with your GitHub account
2. Click "New +" → "Web Service"
3. Connect your `kargah` GitHub repository
4. Fill in the settings:
   - **Name:** kargah-api
   - **Root Directory:** kargah-app/backend
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Click "Create Web Service"
6. Wait 2–3 minutes for the first deploy

When it finishes, Render gives you a URL like `https://kargah-api.onrender.com`.

Test it: open `https://kargah-api.onrender.com/masters` in your browser — you should see your master data.

**Step 3 — Update your README**

In `kargah-app/README.md`, replace `[your GitHub Pages link if deployed]` with your real Render URL.

**Step 4 — Note the limitation (important to know)**

Free Render instances "sleep" after 15 minutes of inactivity. The first request after sleeping takes ~30 seconds to wake up. Mention this in demos: "It's on a free tier so the first load is slow — after that it's fast."

**Step 5 — Git commit**
```
git add .
git commit -m "week12-mon: deploy to Render, add live URL to README"
git push
```

---

## Tuesday — Explain Your Own Code

**The hardest interview question: "Walk me through your code."**

For each of these files, write a 3-sentence explanation (in English, out loud):
- `backend/main.py` — "This file is the FastAPI application. It defines all the API endpoints..."
- `backend/database.py` — "This file..."
- `frontend/js/main.js` — "This file..."
- `frontend/js/master.js` — "This file..."

Then ask Claude:
```
Ask me to explain how the Kargah master listing works — from the user clicking 
the page to data appearing on screen. Interrupt me if I say something wrong or vague.
I want to practice answering technical interview questions about my own project.
```

**Git commit:**
```
git add .
git commit -m "week12-wed: code explanation practice"
```

---

## Tuesday — Full Demo Run

**Practice your demo — 5 minutes, no notes:**

1. Open the browser. Backend running.
2. "Kargah is a marketplace for Iranian craft masters — like Airbnb but for traditional skills."
3. Show the master listing. Filter by city.
4. Click Hossein's profile. "He offers three types of sessions."
5. Fill in the booking form. Submit. "The seeker has submitted a request."
6. Open the admin panel. "The master or admin can see the request here."
7. Add a new session. "They can add new sessions any time."
8. "This is built with Python FastAPI on the backend, SQLite as the database, and vanilla JavaScript on the frontend — no frameworks."

Record yourself (phone is fine). Watch it back. Fix the parts that feel weak.

**Git commit:**
```
git add .
git commit -m "week12-thu: demo rehearsal complete"
```

---

## Wednesday — Final Push + Career Reflection

**Step 1 — Final push**
```bash
git add .
git commit -m "week12-fri: final weekly log"
git push
```

**Step 2 — Count your commits**
```bash
git log --oneline | wc -l
```

You should have 50+ commits. This is your commit history. It proves you showed up every day.

**Step 3 — Fill in the final weekly log**

Open `STUDENT_WEEKLY_LOG.md`. Fill in Week 12. Be honest:
- Which part of the stack did you enjoy most?
- Frontend, backend, databases, or something else?
- What was the hardest concept?
- What would you build next?

**Step 4 — What comes next**

Based on what you enjoyed most, here's your next step:

| If you loved... | Learn next |
|---|---|
| Backend + APIs | Django REST Framework → PostgreSQL → Redis |
| Frontend + UI | React → TypeScript → Next.js |
| Databases + data | PostgreSQL → Python data libraries → SQL deep dive |
| DevOps + systems | Docker in depth → Linux → Nginx → CI/CD |
| All of it | Keep building — add a feature to Kargah every week |

---

**CONGRATULATIONS.**

You started with zero coding knowledge and built a real web product.
You have 50+ Git commits on GitHub.
You can explain how the web works, how databases work, how APIs work, and how to connect all three.

That is a junior developer.

---

## Final Checklist — All 12 Weeks

**Foundation:**
- [ ] You understand CPU, RAM, process, thread
- [ ] You can explain what happens when you type a URL
- [ ] You know TCP vs UDP, HTTP vs HTTPS

**Tools:**
- [ ] Git: daily commits, branches, merges — 50+ commits
- [ ] VS Code: comfortable editing, terminal, Live Server
- [ ] Claude/AI: using prompt templates, not copy-pasting blindly

**Python:**
- [ ] Variables, functions, classes, error handling
- [ ] List comprehensions, sorting, JSON
- [ ] Making HTTP requests with `requests`
- [ ] Understanding Big O and when it matters

**HTML + CSS:**
- [ ] Semantic HTML structure
- [ ] Box model, flexbox, responsive design
- [ ] Connecting CSS to HTML

**JavaScript:**
- [ ] Variables, functions, arrow functions
- [ ] DOM manipulation
- [ ] fetch() + async/await
- [ ] Event listeners

**FastAPI:**
- [ ] GET and POST endpoints
- [ ] Path and query parameters
- [ ] Pydantic models for validation
- [ ] CORS middleware

**Database:**
- [ ] SELECT, WHERE, JOIN, GROUP BY
- [ ] INSERT, UPDATE, DELETE
- [ ] Normalization and indexes
- [ ] Transactions and ACID

**Full Stack:**
- [ ] Frontend fetches from backend
- [ ] Booking form submits to API → stored in DB
- [ ] Admin panel CRUD operations
- [ ] Kargah is deployed live (real URL, not localhost)

**Testing:**
- [ ] pytest installed and understood
- [ ] 5 API endpoint tests written and passing
- [ ] Can explain what a test does and why it matters

**Security:**
- [ ] Password hashing with bcrypt
- [ ] JWT for authentication
- [ ] SQL injection prevention
- [ ] XSS awareness

**Product:**
- [ ] User stories with acceptance criteria
- [ ] Sprint planning
- [ ] PRD written
- [ ] Demo script practiced

---

*You are not a student anymore. You're a developer.*
