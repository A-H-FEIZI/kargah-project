# Interview Preparation Guide — Kargah Project

> Target companies: Snapp, Digikala, Cafe Bazaar, Divar, Tapsi, Balad, and similar Iranian tech leaders
> Timeline: Study this alongside Weeks 11–12. Review it in Month 4 if you have extra time.

---

## What Junior Interviews in Iran Actually Look Like

Iranian tech companies at the junior/trainee level test for:

1. **Can you think logically?** — Basic problem solving, not algorithm mastery
2. **Do you understand how the web works?** — HTTP, client-server, databases
3. **Can you talk about something you built?** — Your Kargah project is your answer here
4. **Are you a person worth investing in?** — Curiosity, honesty, ability to learn

They are NOT looking for 10 years of experience. They ARE looking for someone who built something real and can explain it clearly.

---

## Section 1: Technical Questions

### Computer Science Fundamentals

**Q: What is the difference between a compiled and interpreted language?**
A (simple version): Compiled languages (like C) are translated entirely before running. Interpreted languages (like Python) are translated line by line as they run. Python is interpreted — that's why you can run a Python script directly without a separate build step.

**Q: What is RAM vs storage?**
A: RAM is temporary fast memory — it's lost when you turn off the computer. Storage (hard drive/SSD) is permanent. Programs run in RAM; files are saved in storage.

**Q: What is an operating system?**
A: Software that manages hardware resources (CPU, RAM, storage) and lets other programs run. Windows, Linux, and macOS are operating systems.

---

### Networking (his strong area — prepare to shine here)

**Q: What is an IP address?**
A: A unique address that identifies a device on a network, like a home address for computers.

**Q: What is DNS?**
A: Domain Name System — it translates human-readable domain names (like google.com) into IP addresses that computers use to connect.

**Q: What is HTTP? What is HTTPS?**
A: HTTP is the protocol browsers use to communicate with servers. HTTPS is the secure version — all data is encrypted. When you see a padlock in a browser, that's HTTPS.

**Q: What is the difference between TCP and UDP?**
A: TCP guarantees delivery (like certified mail — you know it arrived). UDP is faster but doesn't guarantee delivery (like a radio broadcast). Web browsing uses TCP; video streaming sometimes uses UDP.

---

### Web Development

**Q: What happens when you type a URL in a browser?**
A (complete answer): 
1. Browser asks DNS to translate the domain to an IP address
2. Browser sends an HTTP GET request to that IP address
3. The server receives the request and sends back HTML/CSS/JS
4. Browser renders the HTML into a visible page

**Q: What is a REST API?**
A: An API (Application Programming Interface) is a way for programs to talk to each other. REST is a set of rules for designing web APIs. A REST API uses HTTP methods: GET to read data, POST to create, PUT/PATCH to update, DELETE to remove.

**Q: What is the difference between GET and POST?**
A: GET retrieves data (like searching). POST sends data to create something (like submitting a form). GET parameters are visible in the URL; POST data is in the request body.

**Q: What is JSON?**
A: JavaScript Object Notation — a text format for sending structured data between a server and a browser. It looks like this: `{"name": "Ali", "craft": "pottery"}`.

**Q: What is the difference between frontend and backend?**
A: Frontend is everything the user sees and interacts with — HTML, CSS, JavaScript in the browser. Backend is the server-side logic — processing requests, talking to the database, returning data. In Kargah, the artisan listing page is frontend; the `/artisans` API endpoint is backend.

---

### Databases

**Q: What is a database?**
A: An organized collection of data stored so it can be easily accessed and modified. Like a very powerful, structured spreadsheet.

**Q: What is SQL?**
A: Structured Query Language — the language used to interact with relational databases. SELECT, INSERT, UPDATE, DELETE are the core commands.

**Q: What is a primary key?**
A: A unique identifier for each row in a database table. Like an ID number — no two rows can have the same primary key.

**Q: What is a foreign key?**
A: A column in one table that references the primary key of another table, creating a relationship between them. In Kargah, an artisan record has a `category_id` that points to the categories table.

**Q: What is the difference between SQL and NoSQL?**
A: SQL databases store data in structured tables with defined schemas (like SQLite, PostgreSQL). NoSQL databases are more flexible — they can store documents, key-value pairs, etc. (like MongoDB). For most web applications, SQL is the right starting choice.

---

### Python Basics

**Q: What is the difference between a list and a dictionary in Python?**
A: A list is an ordered collection accessed by index (position): `["Ali", "Reza", "Sara"]`. A dictionary stores key-value pairs accessed by key: `{"name": "Ali", "city": "Isfahan"}`.

**Q: What is a function?**
A: A named block of reusable code that takes inputs (parameters), does something, and optionally returns an output.

**Q: What is OOP (Object-Oriented Programming)?**
A (awareness level): A way of organizing code around "objects" that combine data and behavior. A class is a blueprint; an object is an instance. Python supports OOP but you don't have to use it always.

**Practice — Write these from memory:**
```python
# Write a function that returns the longest word in a list
def longest_word(words):
    return max(words, key=len)

# Write a function that counts how many times each word appears
def word_count(sentence):
    words = sentence.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts
```

---

### Testing

**Q: Do you write tests?**
A: "Yes. I used pytest to write integration tests for Kargah's API endpoints. For example, I test that `GET /masters` returns a list, that filtering by city returns only masters from that city, and that posting a booking request succeeds. I learned that tests let you change code confidently — you know immediately if you broke something."

**Q: What is the difference between a unit test and an integration test?**
A: A unit test checks one function in isolation — no database, no network. An integration test checks that multiple parts work together — for example, that an HTTP request reaches the endpoint, the database query runs, and the right JSON comes back. My Kargah tests are integration tests using FastAPI's TestClient.

---

### Git

**Q: What is Git? What is GitHub?**
A: Git is a version control system — it tracks changes to your code over time. GitHub is a cloud platform where you store and share Git repositories.

**Q: What is a branch?**
A: A separate line of development. You create a branch to work on a feature without affecting the main code. When done, you merge it back.

**Q: What is a pull request?**
A: A request to merge your branch into the main branch. It's a code review process — others can comment on your changes before they're merged.

**Know these commands cold:**
```bash
git init           # initialize a repo
git add .          # stage all changes
git commit -m ""   # commit with message
git push           # upload to GitHub
git pull           # download latest changes
git branch         # list branches
git checkout -b feature-name   # create and switch to new branch
git merge feature-name         # merge branch into current
git log --oneline  # see commit history
```

---

## Section 2: Behavioral Questions (STAR Method)

**STAR = Situation, Task, Action, Result**

Every behavioral answer should follow this structure in 60–90 seconds.

---

**Q: Tell me about yourself.**
Template: "I'm a computer engineering student at Azad University. Over the past 3 months, I built a web platform called Kargah for discovering traditional Iranian artisans. Before this, I worked as a network technician for 6 months, which gave me a strong understanding of how infrastructure works. I'm particularly drawn to [backend development / frontend / whichever path he chose], and I'm looking for an environment where I can keep learning fast."

---

**Q: Tell me about a project you built.**
Template: "I built Kargah — a platform for discovering traditional Iranian artisans. It has a FastAPI backend, SQLite database, and a JavaScript frontend. Users can browse artisans by category, search by city, and view portfolio profiles. An admin panel lets the owner add and manage artisan listings. I built it over 3 months, starting from zero coding knowledge, and used Git throughout so you can see every step in my commit history."

---

**Q: What was the hardest technical problem you solved?**
Think back to the specific moment in Kargah where something was truly broken and you fixed it. Name the exact problem, what you tried, what worked.

---

**Q: What do you do when you're stuck?**
Good answer: "First I re-read the error message carefully — most errors explain what went wrong. Then I search Stack Overflow with the exact error text. If I'm still stuck after 30 minutes, I reach out to my mentor. I've learned that being stuck for hours alone is less useful than a 5-minute conversation with someone who knows the answer."

---

**Q: Why [company name]?**
Research the company before each interview. Know 2–3 products they build. Know one technical challenge their industry faces. Connect your interest to something real.

---

**Q: Where do you see yourself in 2 years?**
Be honest about your path preference. "I want to become a solid [backend developer / frontend developer / etc.]. In 2 years, I want to be someone who can independently design and build a feature from database schema to user interface — and mentor someone newer than me."

---

**Q: What is your biggest weakness?**
Pick something real but not disqualifying, and always follow with what you're doing about it.
Example: "I'm still slow at reading English documentation, so sometimes tasks take me longer than they should. I've been deliberately reading English docs instead of always switching to Persian sources, and it's getting faster."

---

## Section 3: The Kargah Demo Script

When asked to demo your project (5–10 minutes):

1. **(1 min) Context** — "Kargah is a discovery platform for traditional Iranian artisans. The problem it solves is that millions of Iranian craftspeople have no digital presence."

2. **(1 min) Architecture overview** — Draw or show a simple diagram: Browser → JavaScript frontend → FastAPI backend → SQLite database

3. **(3 min) Live demo** — Browse categories → click an artisan → show the profile → show search working → show admin login → add a new artisan

4. **(2 min) Code walk** — Open VS Code. Show the FastAPI endpoint that powers the artisan listing. Show the database schema. Show one Git commit and explain what changed.

5. **(1 min) What I'd build next** — "If I had another month, I'd add a review system and look into integrating a payment gateway for booking requests."

---

## Section 4: Company-Specific Notes

| Company | Focus Area | Tip |
|---|---|---|
| **Snapp** | Ride-hailing platform, high-scale backend | They care about scale and reliability. Mention you understand that a `/artisans` endpoint serving millions of requests needs caching and optimization. |
| **Digikala** | E-commerce, large catalog | They think in terms of products, SKUs, inventory. Kargah's artisan profiles are like product listings — draw that parallel. |
| **Cafe Bazaar** | App store, large user base | They value product thinking. Mention you wrote a PRD for a Kargah feature. |
| **Divar** | Classified ads, search-heavy | Their core is search and filtering — you built exactly that in Kargah. |
| **Tapsi** | Ride-hailing | Similar to Snapp. Backend reliability, clean APIs. |
| **Balad** | Maps and local discovery | Most directly relevant to Kargah. Local discovery is their core. |

---

## Section 5: Interview Day Checklist

**Before:**
- [ ] Sleep 8 hours the night before
- [ ] Review your STAR answers one time
- [ ] Open Kargah locally and make sure it runs
- [ ] Know the company's main products
- [ ] Bring your laptop or have GitHub open on your phone

**During:**
- [ ] It's okay to say "I don't know, but here's how I'd figure it out"
- [ ] Think out loud — they want to hear your reasoning, not just your answer
- [ ] If you don't understand a question, ask them to rephrase it
- [ ] Slow down. Speaking too fast is a nervous habit.

**After:**
- [ ] Send a follow-up message within 24 hours thanking them
- [ ] Write down every question they asked — use it to prepare for the next interview

---

*This guide should be reviewed weekly during Month 3 and practiced aloud, not just read.*
