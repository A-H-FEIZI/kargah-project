# کارگاه — برنامه هفتگی ۱۲ هفته‌ای
### این فایل را هر روز باز کن. هفته جاری را پیدا کن. کارهای امروز را به ترتیب انجام بده.

---

## چطور از این فایل استفاده کنی

- **صبح**: قبل از هر چیز کارهای امروز را بخوان.
- **در حین کار**: `PROMPT_CHEATSHEET_FA.md` را در یک تب دیگر VS Code باز نگه‌دار.
- **آخر هر روز**: `git add . && git commit -m "پیام کامیت"` را بزن — حتی اگر هیچ چیز کار نمی‌کند.
- **هر چهارشنبه**: `STUDENT_WEEKLY_LOG.md` را پر کن و کامیت بزن.

---

# هفته ۱ — کامپیوتر و اینترنت واقعاً چطور کار می‌کنند

**هدف یادگیری:** بفهمی وقتی یک آدرس سایت می‌زنی، از کیبورد تا صفحه‌نمایش چه اتفاقی می‌افتد.
**هدف کارگاه:** پروژه روی GitHub باشد و محیط توسعه کار کند.

> ستاپ روز اول (VS Code، Git، GitHub، اولین کامیت) در `START_HERE.md` است. اول آن را کامل کن.
---

## شنبه — ماشین زیر کد

**چه یاد می‌گیری:** CPU، RAM، حافظه، پروسس، ترد — واقعیت فیزیکی که کدت روی آن اجرا می‌شود.

**قدم ۱ — بخوان (۲۰ دقیقه)**

آدرس زیر را در مرورگر باز کن و از اول تا آخر بخوان:
`https://cs.fyi/guide/how-does-internet-work`

در حین خواندن، یک فایل جدید در VS Code بساز: `notes/week1.md`
به هر سوال یک جواب یک‌جمله‌ای بنویس:
- CPU چیست؟
- RAM چیست و چرا با خاموش کردن کامپیوتر پاک می‌شود؟
- پروسس چیست؟
- ترد چیست و چه فرقی با پروسس دارد؟

**قدم ۲ — از Claude بپرس (۱۵ دقیقه)**

claude.ai را باز کن و این پرامپت را paste کن:
```
تفاوت پروسس و ترد را مثل یک نفر توضیح بده که کامپیوتر بلد است 
اما هیچوقت کد ننوشته. از یک تشبیه آشپزی استفاده کن. 
بعد یک مثال کوچک Python نشانم بده که دو ترد همزمان کار می‌کنند.
```

جواب Claude را بخوان. مثال Python را در `notes/week1.md` با یک یادداشت کپی کن.

**قدم ۳ — اجرا کن (۱۵ دقیقه)**

ترمینال VS Code را باز کن (`Ctrl + بک‌تیک`). مطمئن شو در پوشه kargah هستی.

فایل `experiments/threads_demo.py` را بساز:
```python
import threading
import time

def task(name, seconds):
    print(f"{name} شروع شد")
    time.sleep(seconds)
    print(f"{name} بعد از {seconds} ثانیه تموم شد")

t1 = threading.Thread(target=task, args=("کار الف", 2))
t2 = threading.Thread(target=task, args=("کار ب", 1))

t1.start()
t2.start()

t1.join()
t2.join()

print("هر دو تموم شدن")
```

اجرا کن: `python experiments/threads_demo.py`

توجه کن: کار ب قبل از کار الف تموم می‌شه، در حالی که الف را اول شروع کردی. این همان ترد است.

**قدم ۴ — کامیت Git**
```
git add .
git commit -m "week1-mon: add thread demo and notes"
```

---

## یکشنبه — اینترنت چطور کار می‌کند

**چه یاد می‌گیری:** وقتی یک URL می‌زنی، واقعاً چه اتفاقی می‌افتد.

**قدم ۱ — تماشا کن (۲۰ دقیقه)**

در YouTube جستجو کن: `"DNS explained in 5 minutes"` — اولین نتیجه از ByteByteGo یا مشابه را ببین.

بعد این صفحه کوتاه را بخوان: `https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview`
(نیازی نیست همه چیز را بخوانی — فقط ۴ بخش اول.)

**قدم ۲ — در یادداشت‌هایت نقشه بکش**

در `notes/week1.md`، این ترتیب را با کلمات خودت بنویس:
```
می‌زنی: kargah.ir
← کامپیوترت از [؟] آدرس IP می‌پرسد
← [؟] با [؟] جواب می‌دهد
← مرورگرت یک درخواست [؟] به [؟] می‌فرستد
← سرور با [؟] جواب می‌دهد
← مرورگرت [؟] را رندر می‌کند
```

هر [؟] را پر کن. اگر گیر کردی از Claude بپرس:
```
مبتدی هستم. دقیقاً وقتی یک URL می‌زنم و Enter می‌کنم چه اتفاقی می‌افتد — 
از DNS lookup تا صفحه روی صفحه‌نمایش. زبان ساده استفاده کن. 
هر قدم را شماره بزن.
```

**قدم ۳ — Git کامیت**
```
git add .
git commit -m "week1-tue: web request notes and DNS explanation"
```

---

## دوشنبه — HTTP، TCP، و پروتکل‌ها

**چه یاد می‌گیری:** فرق HTTP، HTTPS، TCP، UDP — و اینکه چرا مهم است.

**قدم ۱ — بخوان و بپرس (۲۵ دقیقه)**

بخوان: `https://roadmap.sh/guides/http-basics` (فقط نیمه اول — تا "HTTP Methods")

بعد از Claude بپرس:
```
فرق TCP و UDP را با یک تشبیه از دنیای واقعی توضیح بده. 
بعد توضیح بده چرا HTTP از TCP استفاده می‌کند نه UDP. 
ساده باشد — تازه شروع کردم به یادگیری.
```

نکات مهم را در `notes/week1.md` اضافه کن.

**قدم ۴ — Git کامیت**
```
git add .
git commit -m "week1-wed: HTTP methods notes and curl experiments"
```

---

## سه‌شنبه — شبکه‌ها، پروکسی، VPN

**چه یاد می‌گیری:** آدرس IP، فایروال، پروکسی، ریورس پروکسی، VPN، CDN — این کلمه‌ها را شنیدی. حالا می‌فهمی واقعاً چه کار می‌کنند.

**قدم ۱ — از Claude بپرس (۲۰ دقیقه)**

این پرامپت را paste کن:
```
سابقه مهندسی شبکه دارم. این مفاهیم شبکه را از دیدگاه یک توسعه‌دهنده نرم‌افزار توضیح بده:
۱. پروکسی vs ریورس پروکسی
۲. VPN — تکنیکی چه کار می‌کند
۳. فایروال — یک توسعه‌دهنده باید چه چیزی را کانفیگ کند
۴. CDN — چه کار می‌کند و کِی استفاده کنیم
۵. لود بالانسر — توضیح ساده

برای هر کدام یک جمله بگو "چرا یک توسعه‌دهنده به این اهمیت می‌دهد."
```

**قدم ۲ — به کارگاه وصل کن**

در `notes/week1.md` جواب بده:
- وقتی کارگاه راه بیفتد و ۱۰,۰۰۰ کاربر همزمان داشته باشد — به کدام یک از این مفاهیم نیاز داریم؟
- چرا کارگاه به HTTPS نیاز دارد نه فقط HTTP؟

**قدم ۳ — Git کامیت**
```
git add .
git commit -m "week1-thu: network concepts notes - proxy CDN VPN"
```

---

## چهارشنبه — مرور + لاگ هفتگی

**قدم ۱ — خودت را آزمون کن (۲۰ دقیقه)**

از Claude بپرس:
```
مرا روی این موضوعات آزمون بگیر — یک سوال در یک زمان. منتظر جوابم باش.
بعد از هر جواب بگو چه چیزی درست گفتم و چه چیزی از قلم انداختم.

موضوعات: پروسس vs ترد، DNS چطور کار می‌کند، فرق HTTP و HTTPS، 
پروکسی چه کار می‌کند، CDN چه کار می‌کند، TCP vs UDP.
```

**قدم ۲ — لاگ هفتگی را پر کن**

`STUDENT_WEEKLY_LOG.md` را باز کن. بخش هفته ۱ را صادقانه پر کن.

**قدم ۳ — Git کامیت**
```
git add .
git commit -m "week1-fri: weekly log + review quiz"
git push
```

**چک‌لیست هفته ۱:**
- [ ] `notes/week1.md` با توضیحات خودت وجود دارد
- [ ] `experiments/threads_demo.py` وجود دارد و اجرایش کردی
- [ ] می‌دانی وقتی URL می‌زنی چه اتفاقی می‌افتد (DNS → TCP → HTTP → HTML)
- [ ] می‌توانی پروسس vs ترد را با کلمات ساده توضیح دهی
- [ ] حداقل ۵ کامیت روی GitHub

---

# هفته ۲ — Git مثل یک حرفه‌ای + پایه‌های Python

**هدف یادگیری:** از Git طوری استفاده کنی که توسعه‌دهندگان واقعی استفاده می‌کنند. اولین توابع Python را بنویسی.
**هدف کارگاه:** مخزن کارگاه با ساختار درست و برنچ‌ها. اولین اسکریپت Python اجرا شود.

---

## شنبه — Git: روش درست

**چه یاد می‌گیری:** Staging، کامیت، برنچ، مرج، پول ریکوئست.

**قدم ۱ — بخوان (۲۰ دقیقه)**

برو به: `https://learngitbranching.js.org/`

بخش **Introduction Sequence** لِوِل‌های ۱ تا ۴ را کامل کن (تعاملی است — دستورات git واقعی می‌زنی).

این لِوِل‌ها را پوشش می‌دهند: commit، branch، checkout، merge.

**قدم ۲ — در پروژه واقعی تمرین کن (۲۰ دقیقه)**

در ترمینال پوشه kargah:
```bash
git status
git log --oneline

# یک برنچ برای یادداشت‌هایت بساز
git checkout -b feature/week2-practice

# فایل notes/week2.md را در VS Code بساز، "یادداشت‌های هفته ۲" بنویس
git add notes/week2.md
git commit -m "week2: add notes file"

# به main برگرد
git checkout main

# برنچت را مرج کن
git merge feature/week2-practice

git push
```

**قدم ۳ — Git کامیت**
```
git add .
git commit -m "week2-mon: git branching practice"
```

---

## یکشنبه — Python: متغیر، تابع، لیست، دیکشنری

**چه یاد می‌گیری:** بلوک‌های سازنده که هر روز در بک‌اند کارگاه استفاده می‌کنی.

**قدم ۱ — بخوان و امتحان کن (۳۰ دقیقه)**

فایل `experiments/python_basics.py` را بساز و این‌ها را **با دست بنویس** (کپی-پیست نکن):

```python
# متغیرها
name = "کارگاه"
version = 1
is_live = False

print(name, version, is_live)

# لیست‌ها
masters = ["حسین کلهر", "زهرا شیرازی", "علی ابراهیمی"]
print(masters[0])
print(len(masters))
masters.append("سارا نظری")
print(masters)

# دیکشنری‌ها
master = {
    "name": "حسین کلهر",
    "city": "تهران",
    "craft": "قالی‌بافی",
    "years_exp": 15
}
print(master["name"])
print(master.get("rating", "هنوز امتیاز ندارد"))

# حلقه‌ها
for m in masters:
    print(f"استاد: {m}")
```

اجرا کن: `python experiments/python_basics.py`

**قدم ۲ — توابع (۲۰ دقیقه)**

به همان فایل اضافه کن:

```python
def greet_master(name, city):
    return f"خوش آمدی، {name} از {city}!"

message = greet_master("حسین", "تهران")
print(message)

def filter_by_city(masters_list, city):
    result = []
    for master in masters_list:
        if master["city"] == city:
            result.append(master)
    return result

all_masters = [
    {"name": "حسین", "city": "تهران"},
    {"name": "زهرا", "city": "اصفهان"},
    {"name": "علی", "city": "تهران"},
]

tehran_masters = filter_by_city(all_masters, "تهران")
print(tehran_masters)
```

**قدم ۳ — Git کامیت**
```
git add .
git commit -m "week2-tue: python basics - variables functions lists dicts"
```

---

## دوشنبه — Python: کلاس و مدیریت خطا

فایل `experiments/python_classes.py` را بساز:

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
        return f"{self.name} — استاد {self.craft} از {self.city}"

hossein = Master("حسین کلهر", "تهران", "قالی‌بافی")
hossein.add_session("studio", "۵۰۰,۰۰۰ تومان")
hossein.add_session("سیار", "۸۰۰,۰۰۰ تومان")

print(hossein.describe())
print(hossein.sessions)
```

مدیریت خطا اضافه کن:
```python
def get_city(master_dict):
    try:
        return master_dict["city"]
    except KeyError:
        return "شهر وارد نشده"

print(get_city({"name": "علی"}))
print(get_city({"name": "علی", "city": "تهران"}))
```

```
git add .
git commit -m "week2-wed: python classes and error handling"
```

---

## سه‌شنبه — Python: فایل و JSON

فایل `experiments/json_practice.py` را بساز:

```python
import json

master = {
    "name": "حسین کلهر",
    "city": "تهران",
    "sessions": ["studio", "سیار"]
}

json_string = json.dumps(master, ensure_ascii=False, indent=2)
print(json_string)

parsed = json.loads(json_string)
print(parsed["city"])

with open("experiments/master_data.json", "w", encoding="utf-8") as f:
    json.dump(master, f, ensure_ascii=False, indent=2)

with open("experiments/master_data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded["name"])
```

```
git add .
git commit -m "week2-thu: python files and JSON practice"
```

---

## چهارشنبه — چالش + لاگ هفتگی

بدون نگاه به یادداشت‌هایت، از صفر یک تابع بنویس:
```
تابعی به نام search_masters(masters_list, city, craft) بنویس.
یک لیست از دیکشنری‌های استاد می‌گیرد و فقط آن‌هایی را برمی‌گرداند که city AND craft مطابقت دارند.
اگر city برابر None بود، هر شهری را قبول کن.
اگر craft برابر None بود، هر رشته‌ای را قبول کن.
```

```
git add .
git commit -m "week2-fri: challenge and weekly log"
git push
```

---

# هفته ۳ — Python پیشرفته + اولین فراخوانی API

**هدف:** Python بنویسی که داده واقعی از اینترنت می‌گیرد.
**هدف کارگاه:** اسکریپت Python که با یک API صحبت می‌کند.

*(هفته‌های ۳ تا ۱۲ — ساختار مشابه هفته‌های قبل. برای جزئیات کامل به `WEEKLY_PLAN_EN.md` مراجعه کن.)*

---

## شنبه — List Comprehension و مرتب‌سازی

```python
masters = [
    {"name": "حسین", "city": "تهران", "years_exp": 15, "price": 500000},
    {"name": "زهرا", "city": "اصفهان", "years_exp": 8, "price": 350000},
    {"name": "علی", "city": "تهران", "years_exp": 20, "price": 750000},
]

# List comprehension
names = [m["name"] for m in masters]

# با فیلتر
tehran = [m for m in masters if m["city"] == "تهران"]

# مرتب‌سازی بر اساس قیمت
by_price = sorted(masters, key=lambda m: m["price"])
for m in by_price:
    print(f"{m['name']}: {m['price']:,} تومان")
```

```
git commit -m "week3-mon: list comprehensions and sorting"
```

---

## یکشنبه — درخواست HTTP از Python

```bash
pip install requests
```

```python
import requests

response = requests.get("https://httpbin.org/json")
print(response.status_code)
print(response.json())

params = {"city": "تهران"}
response = requests.get("https://httpbin.org/get", params=params)
print(response.json()["args"])
```

```
git commit -m "week3-tue: http requests with Python requests library"
```

---

## دوشنبه — Big-O: چرا بعضی کدها کند هستند

از Claude بپرس:
```
نشانه‌گذاری Big O را برای یک توسعه‌دهنده که تازه شروع کرده توضیح بده.
از یک تشبیه سوپرمارکت استفاده کن.
بعد نمونه‌های Python برای O(1)، O(n)، O(n²) نشانم بده.
نشان بده چرا O(n²) برای ۱۰,۰۰۰ استاد در کارگاه فاجعه‌بار است.
```

```
git commit -m "week3-wed: big-O notation"
```

---

## سه‌شنبه — ساختار داده‌ها

از Claude بپرس:
```
این ساختارهای داده را با یک تشبیه از دنیای واقعی توضیح بده:
۱. آرایه / لیست
۲. هش مپ / دیکشنری
۳. پشته (LIFO)
۴. صف (FIFO)
۵. درخت باینری

برای هر کدام یک مثال مشخص بده که کارگاه از آن استفاده می‌کند.
```

```
git commit -m "week3-thu: data structures"
```

---

# هفته ۴ — HTML + CSS: ساختن صورت کارگاه

**هدف یادگیری:** HTML و CSS بنویسی که یک صفحه وب واقعی بسازد.
**هدف کارگاه:** صفحه لیست استادان (`index.html`) ساخته و استایل داده شده باشد.

---

## شنبه — HTML: اول ساختار

فایل `kargah-app/frontend/index.html` را باز کن و بخوان.

در `notes/week4.md` جواب بده:
- `<head>` چه چیزی دارد؟ `<body>` چه چیزی دارد؟
- `<div class="master-card">` چیست؟ attribute `class` چه کار می‌کند؟

این `<header>` را به بالای `<body>` اضافه کن:
```html
<header class="site-header">
  <div class="container">
    <h1 class="logo">کارگاه</h1>
    <p class="tagline">با استادان هنرهای سنتی آشنا شو</p>
  </div>
</header>
```

```
git checkout -b feature/week4-frontend
git commit -m "week4-mon: add site header to index.html"
```

---

## یکشنبه — CSS: واقعی به نظر رسیدن

بازی Flexbox Froggy را انجام بده: `https://flexboxfroggy.com/`

این استایل را در `style.css` اضافه کن:
```css
.site-header {
  background: var(--primary);
  color: white;
  padding: 1.5rem 0;
  text-align: center;
}

.masters-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  padding: 2rem;
}

@media (max-width: 768px) {
  .masters-grid {
    flex-direction: column;
    padding: 1rem;
  }
}
```

```
git commit -m "week4-wed: CSS flexbox and responsive design"
```

---

## چهارشنبه — مرج و پوش

```bash
git checkout main
git merge feature/week4-frontend
git push
```

---

# هفته ۵ — جاوااسکریپت: صفحات تعاملی

**هدف:** JS بنویسی که داده می‌خواند و صفحه را به‌صورت داینامیک آپدیت می‌کند.
**هدف کارگاه:** صفحه لیست استادان داده‌های واقعی را لود و رندر می‌کند.

---

## یکشنبه — DOM: جاوااسکریپت با HTML ملاقات می‌کند

فایل `experiments/dom_practice.html` را بساز:
```html
<!DOCTYPE html>
<html>
<body>
  <h1>استادان</h1>
  <div id="master-list"></div>

  <script>
    const masters = [
      { name: "حسین کلهر", craft: "قالی‌بافی", city: "تهران" },
      { name: "زهرا شیرازی", craft: "نگارگری", city: "اصفهان" },
    ];

    const container = document.getElementById("master-list");

    masters.forEach(master => {
      const card = document.createElement("div");
      card.innerHTML = `
        <h2>${master.name}</h2>
        <p>${master.craft} — ${master.city}</p>
      `;
      container.appendChild(card);
    });
  </script>
</body>
</html>
```

---

## دوشنبه — fetch() و Async/Await

از Claude بپرس:
```
Event loop جاوااسکریپت را توضیح بده و اینکه چرا fetch() غیرهمزمان است — 
با یک تشبیه رستوران. 
بعد فرق callback، .then()، و async/await را برای همان fetch نشان بده.
```

```javascript
button.addEventListener("click", async () => {
  try {
    const response = await fetch("https://httpbin.org/json");
    const data = await response.json();
    result.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
  } catch (error) {
    result.textContent = `خطا: ${error.message}`;
  }
});
```

---

# هفته ۶ — FastAPI: ساختن بک‌اند کارگاه

**هدف:** یک REST API واقعی بسازی که داده از Python برمی‌گرداند.
**هدف کارگاه:** بک‌اند به‌صورت لوکال در حال اجرا باشد و داده واقعی به فرانت‌اند بدهد.

---

## شنبه — معرفی FastAPI

```bash
pip install fastapi uvicorn
```

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/masters")
def list_masters():
    return [
        {"id": 1, "name": "حسین کلهر", "city": "تهران"},
        {"id": 2, "name": "زهرا شیرازی", "city": "اصفهان"},
    ]
```

```bash
uvicorn experiments.first_api:app --reload
```

مرورگر را باز کن: `http://localhost:8000/masters`

همچنین: `http://localhost:8000/docs` — FastAPI به‌صورت خودکار مستندات تولید می‌کند!

---

## دوشنبه — اجرای بک‌اند واقعی کارگاه

```bash
# از پوشه kargah-app/backend/
pip install fastapi uvicorn
python database.py
python seed_data.py
uvicorn main:app --reload
```

تست کن:
- `http://localhost:8000/masters`
- `http://localhost:8000/masters?city=تهران`
- `http://localhost:8000/sessions?type=mobile`
- `http://localhost:8000/docs`

---

# هفته ۷ — دیتابیس: SQLite و SQL

**هدف یادگیری:** دیتابیس‌های رابطه‌ای را بفهمی و کوئری SQL واقعی بنویسی.
**هدف کارگاه:** هر جدول در `database.py` را بفهمی.

---

## شنبه — دیتابیس چیست و چرا SQL؟

از Claude بپرس:
```
چرا یک اپ production نمی‌تواند فقط داده را در لیست‌های Python نگه‌دارد؟
دیتابیس رابطه‌ای چیست — با یک تشبیه صفحه گسترده.
SQLite چیست و کِی خوب است و کِی کافی نیست؟
```

DB Browser for SQLite را نصب کن: `https://sqlitebrowser.org/dl/`

فایل `kargah-app/backend/kargah.db` را باز کن.

---

## یکشنبه — SQL: SELECT، WHERE، JOIN

در DB Browser → تب SQL:

```sql
-- همه استادان
SELECT * FROM masters;

-- فقط استادان تهران
SELECT name, city, years_exp FROM masters WHERE city = 'تهران';

-- ۳ استاد با بیشترین تجربه
SELECT name, years_exp FROM masters ORDER BY years_exp DESC LIMIT 3;

-- JOIN: عنوان جلسه + نام استاد
SELECT sessions.title, sessions.type, masters.name AS master_name
FROM sessions
JOIN masters ON sessions.master_id = masters.id;
```

---

# هفته ۸ — فول‌استک: فرانت‌اند با بک‌اند

**هدف:** ویژگی‌ها را از انتها به انتها بسازی — از کلیک دکمه تا دیتابیس و برگشت.
**هدف کارگاه:** فرم رزرو کار کند. صفحه جلسات لود شود. پروفایل استاد کامل باشد.

---

## شنبه — فلو رزرو از انتها به انتها

در `notes/week8.md` فلوی کامل را بنویس:
```
۱. کاربر فرم را در [کدام فایل HTML؟] پر می‌کند
۲. کاربر "ارسال" می‌کند
۳. JavaScript [چه کاری می‌کند؟]
۴. fetch() یک درخواست [GET/POST؟] به [کدام URL؟] می‌فرستد
۵. FastAPI آن را در [کدام endpoint؟] دریافت می‌کند
۶. Python [چه validation؟] انجام می‌دهد
۷. SQL اجرا می‌شود: [چه کوئری؟]
۸. پاسخ برگشت می‌آید: [چه JSON؟]
۹. JavaScript [صفحه را چطور آپدیت می‌کند؟]
```

---

# هفته ۹ — تفکر محصول + برنامه‌ریزی Sprint

**هدف یادگیری:** مثل یک product manager فکر کنی. نیازمندی‌هایی بنویسی که مهندس‌ها بتوانند بسازند.
**هدف کارگاه:** پنل ادمین کار کند. User story نوشته شود.

---

## شنبه — User Story چیست؟

از Claude بپرس:
```
۸ user story برای کارگاه بنویس — ۴ از دیدگاه جوینده و ۴ از دیدگاه استاد.
فرمت: "به عنوان یک [نقش]، می‌خواهم [عمل] تا [فایده]."
برای هر story، ۳ معیار پذیرش به فرمت Given/When/Then اضافه کن.
```

---

# هفته ۱۰ — Docker + تکمیل محصول

**هدف:** کانتینرها را بفهمی. بدانی کِی از آن‌ها استفاده کنی.
**هدف کارگاه:** همه صفحات از انتها به انتها کار کنند.

---

## شنبه — Docker چیست؟

از Claude بپرس:
```
Docker را با یک تشبیه آشپزی (دستورالعمل vs غذای واقعی) توضیح بده.
Image vs Container چیست؟
Dockerfile چیست؟
چرا از Docker برای کارگاه در production استفاده می‌کنم؟
docker-compose چیست؟
```

---

## یکشنبه-دوشنبه — تکمیل همه صفحات

**چک‌لیست هر صفحه:**

`index.html`:
- [ ] استادان از API لود می‌شوند
- [ ] فیلتر شهر کار می‌کند
- [ ] هر کارت به صفحه پروفایل لینک دارد

`sessions.html`:
- [ ] همه جلسات لود می‌شوند
- [ ] فیلتر بر اساس نوع (studio/mobile/commission) کار می‌کند

`master.html`:
- [ ] اطلاعات استاد نمایش داده می‌شود
- [ ] جلسات زیر آن لیست می‌شوند
- [ ] فرم رزرو درست ارسال می‌شود

---

# هفته ۱۱ — امنیت، رمز عبور، و JWT

**هدف یادگیری:** بفهمی authentication و authorization واقعاً چطور کار می‌کنند.
**هدف کارگاه:** لاگین ادمین از رمزهای هش‌شده استفاده کند. JWT مسیرهای ادمین را محافظت کند.

---

## شنبه — رمز عبور: هرگز به صورت متن ساده نگه‌نداری

```bash
pip install bcrypt
```

```python
import bcrypt

def hash_password(plain_password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(plain_password.encode(), salt)
    return hashed.decode()

def verify_password(plain_password: str, hashed: str) -> bool:
    return bcrypt.checkpw(plain_password.encode(), hashed.encode())

password = "kargah2026"
hashed = hash_password(password)
print(f"هش شده: {hashed}")
print(f"رمز صحیح: {verify_password(password, hashed)}")
print(f"رمز اشتباه: {verify_password('wrong', hashed)}")
```

---

## یکشنبه — JWT: توکن‌های لاگین چطور کار می‌کنند

از Claude بپرس:
```
JWT را برای یک مبتدی توضیح بده.
چه فرقی با session cookie دارد؟
سه بخش یک JWT چیست؟
چرا کاربر نمی‌تواند بدون کلید مخفی JWT جعل کند؟
```

---

# هفته ۱۲ — پالایش، آماده‌سازی مصاحبه، و روز نمایش

**هدف:** آنچه ساختی را واضح و با اعتماد به نفس ارائه دهی.
**هدف کارگاه:** GitHub تمیز به نظر برسد. دمو روان باشد. بتوانی سوالات تکنیکی درباره کدت جواب بدهی.

---

## شنبه — README و پالایش GitHub

`kargah-app/README.md` را بنویس:

```markdown
# کارگاه — بازار استادان هنرهای سنتی ایران

یک بازار دوطرفه که استادان سنتی ایرانی را به کسانی که می‌خواهند از آن‌ها یاد بگیرند وصل می‌کند.

**تکنولوژی:** Python + FastAPI + SQLite + HTML/CSS/JavaScript

## امکانات
- لیست استادان با فیلتر شهر و رشته
- سه نوع جلسه: استودیو، سیار، سفارش
- فرم رزرو جلسه
- پنل ادمین برای مدیریت استادان و رزروها

## اجرای لوکال
[مراحل دقیق نصب]
```

---

## یکشنبه — مرور `INTERVIEW_PREP.md`

آن فایل را باز کن. همه بخش‌ها را بخوان.

از Claude بخواه که آزمونت بگیرد:
```
از من سوالات مصاحبه جونیور بپرس — یک سوال در یک زمان.
موضوعات: REST API، SQL، جاوااسکریپت async، Git، HTTP، Python پایه، دیتابیس، امنیت.
منتظر جوابم باش. بگو چه چیزی درست گفتم و چه چیزی از قلم انداختم.
بعد سوال بعدی را بپرس.
```

---

## چهارشنبه — پوش نهایی + تأمل در مسیر شغلی

```bash
git add .
git commit -m "week12-fri: final weekly log"
git push
```

تعداد کامیت‌هایت را بشمار:
```bash
git log --oneline | wc -l
```

باید ۵۰+ کامیت داشته باشی.

---

**تبریک.**

با هیچ دانش کدنویسی شروع کردی و یک محصول وب واقعی ساختی.
۵۰+ کامیت Git روی GitHub داری.
می‌توانی توضیح دهی که وب چطور کار می‌کند، دیتابیس چطور کار می‌کند، API چطور کار می‌کند، و چطور هر سه را به هم وصل کنی.

این همان یک توسعه‌دهنده جونیور است.

---

## چک‌لیست نهایی — همه ۱۲ هفته

**پایه:**
- [ ] CPU، RAM، پروسس، ترد را می‌فهمی
- [ ] وقتی URL می‌زنی چه اتفاقی می‌افتد را توضیح می‌دهی
- [ ] TCP vs UDP، HTTP vs HTTPS را می‌دانی

**ابزارها:**
- [ ] Git: کامیت روزانه، برنچ، مرج — ۵۰+ کامیت
- [ ] VS Code: راحت با ویرایش، ترمینال، Live Server
- [ ] Claude/AI: استفاده از قالب‌های پرامپت، نه کپی‌پیست کور

**Python:**
- [ ] متغیر، تابع، کلاس، مدیریت خطا
- [ ] List comprehension، مرتب‌سازی، JSON
- [ ] درخواست HTTP با `requests`
- [ ] Big O و کِی مهم است

**HTML + CSS:**
- [ ] ساختار HTML معنایی
- [ ] باکس مدل، flexbox، طراحی واکنش‌گرا

**جاوااسکریپت:**
- [ ] متغیر، تابع، arrow function
- [ ] دستکاری DOM
- [ ] fetch() + async/await
- [ ] Event listener

**FastAPI:**
- [ ] endpoint های GET و POST
- [ ] پارامترهای path و query
- [ ] مدل‌های Pydantic

**دیتابیس:**
- [ ] SELECT، WHERE، JOIN، GROUP BY
- [ ] INSERT، UPDATE، DELETE
- [ ] نرمال‌سازی و ایندکس
- [ ] تراکنش و ACID

**فول‌استک:**
- [ ] فرانت‌اند از بک‌اند داده می‌گیرد
- [ ] فرم رزرو ارسال می‌شود و در DB ذخیره می‌شود
- [ ] پنل ادمین CRUD دارد

**امنیت:**
- [ ] هش کردن رمز با bcrypt
- [ ] JWT برای authentication
- [ ] جلوگیری از SQL injection

**محصول:**
- [ ] User story با معیار پذیرش
- [ ] Sprint planning
- [ ] PRD نوشته شده
- [ ] اسکریپت دمو تمرین شده

---

*دیگر دانشجو نیستی. توسعه‌دهنده هستی.*
