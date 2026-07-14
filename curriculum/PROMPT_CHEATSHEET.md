# Prompt Engineering Cheatsheet
### Kargah Project — Keep this open while working

---

## Free AI Tools (no subscription needed)

| Tool | Best For | URL |
|---|---|---|
| **Claude.ai** | Code help, explanations, debugging, long conversations | claude.ai |
| **ChatGPT** | General questions, brainstorming, exercises | chatgpt.com |
| **Google Gemini** | Research, comparing options, Persian content | gemini.google.com |
| **GitHub Copilot** | In-editor code completion (free via GitHub Education) | github.com/features/copilot |
| **Phind** | Coding questions with source references | phind.com |

**Recommendation:** Use **Claude** as your primary tool. It handles long code blocks best and explains reasoning clearly.

---

## The 3 Golden Rules

1. **Never paste AI code without reading every line first.** If you can't explain it, you don't own it.
2. **Use AI to understand, not to skip.** "What does this mean?" not "write this for me."
3. **AI is wrong sometimes — always test what it gives you.**

---

## Prompt Templates by Purpose

Copy these, fill in the blanks `[like this]`, and adjust as needed.

---

### 🔍 The Explainer — when you don't understand a concept

```
Explain [concept] to me. I'm a beginner learning programming for the first time.
Use a simple real-world analogy, then show me a short code example in [Python/JavaScript].
```

**Example:**
> "Explain what a function is to me. I'm a beginner learning programming for the first time.
> Use a simple real-world analogy, then show me a short code example in Python."

---

### 🐛 The Debugger — when you have an error

```
I'm getting this error:
[paste the full error message]

Here's my code:
[paste your code]

I'm a beginner. What's causing this error and how do I fix it?
Explain the fix so I understand why it works.
```

---

### 📝 The Reviewer — when you want feedback on your code

```
Review this [Python/HTML/CSS/JavaScript] code I wrote:

[paste your code]

I'm still learning. Tell me:
1. What did I do well?
2. What mistakes or bad habits do I have?
3. How would you rewrite the worst part to be cleaner?
```

---

### 🎯 The Starter — when you need a working example to study

```
Give me the simplest possible working example of [concept] in [language].
Add a comment on every line explaining what it does.
Don't add anything extra — just the minimum needed to understand the concept.
```

---

### 🧪 The Quiz — when you want to test yourself

```
Quiz me on [topic]. Ask me one question at a time.
Wait for my answer before asking the next one.
After each answer, tell me if I'm right and fill in what I missed.
Start with easy questions and get harder.
```

---

### 🔗 The Connector — when you want to link two concepts

```
I just learned about [concept A].
I've also heard about [concept B] but don't fully understand it.
How do these two things relate to each other?
Give me a concrete example that shows both working together.
```

---

### 🏋️ The Practice Builder — when you want exercises

```
Give me 5 practice exercises on [topic] in [language].
I'm at beginner level.
Start easy and get progressively harder.
Don't give me the answers yet — just the exercises.
```

---

### 🔄 The Refactoring Helper — when you want to improve code

```
Here is my code:
[paste your code]

Rewrite it to be cleaner and easier to read.
After the rewrite, explain every change you made and WHY you made it.
```

---

### 💼 The Interview Prep — when practicing for jobs

```
Ask me a junior [backend/frontend/general] developer interview question.
I'll answer it, then you tell me:
1. What I got right
2. What I missed
3. A model answer I can learn from
Then ask me the next question.
```

---

### 📐 The Architect — when designing something (Week 7+)

```
I'm building [describe your feature in 2 sentences].
I need to store [describe your data].
Suggest a simple database schema (table names, columns, types, relationships).
I'm using SQLite. Explain why you designed it this way.
```

---

### 🚧 The Rubber Duck — when you're stuck and don't know why

```
I'm trying to [what you want to accomplish].
I've tried [what you already tried].
Here's my current code:
[paste code]
I expected [what you expected to happen].
Instead, [what actually happened].
What am I missing?
```

---

## Prompt Patterns for Each Week

| Week | What to Ask AI |
|---|---|
| 1 | "Explain [process/thread/HTTP/DNS] to me like I'm new to computers" |
| 2 | "Quiz me on Git commands" — "What's the difference between git pull and git fetch?" |
| 3 | "Review my Python function" — "Why am I getting this error?" — "Give me 5 Python exercises" |
| 4 | "Review my HTML structure" — "What's wrong with my CSS flexbox layout?" |
| 5 | "Explain JavaScript's event loop with an analogy" — "Debug my fetch() code" |
| 6 | "Explain REST API design to me" — "Review my FastAPI endpoint" |
| 7 | "Help me design the Kargah database schema" — "Explain database normalization" |
| 8 | "Why is my JavaScript not connecting to the API?" — "Explain CORS to me" |
| 9 | "Review my sprint plan for Kargah" — "Write user stories for the master listing feature" |
| 10 | "Explain Docker to me with a cooking analogy" — "Review my admin panel code" |
| 11 | "Quiz me on security vulnerabilities" — "How would you improve my PRD?" |
| 12 | "Give me a junior developer interview question" — "Review my Kargah demo script" |

---

## Prompts for Learning Faster (Meta-learning)

```
I have 3 hours to learn [topic]. I'm a beginner.
Give me a 3-hour study plan with specific tasks and time estimates.
```

```
I just finished reading about [topic].
What are the 3 most common misconceptions beginners have about this?
Test me on each one.
```

```
I understand [topic A] but I'm struggling with [topic B].
What's the conceptual bridge between them I'm probably missing?
```

```
What are 5 things a junior developer should know about [topic] that aren't
obvious from tutorials but matter in real jobs?
```

---

## What NOT to Do

| ❌ Bad Prompt | ✅ Better Prompt |
|---|---|
| "Write me the Kargah API" | "Explain how to design a REST endpoint for listing masters. I'll write the code myself." |
| "Fix my code" | "My code has this error: [error]. Here's the code: [code]. What's wrong and why?" |
| "Is this good?" | "Review this code. Tell me what's wrong and what a better version looks like." |
| "How do I do [topic]?" | "Give me the simplest example of [topic]. Explain every line." |
| "Write a function that..." | "Show me an example of [pattern]. I'll adapt it myself." |

---

*Keep this file open in VS Code. The best developers use AI constantly — the skill is asking smart questions.*
