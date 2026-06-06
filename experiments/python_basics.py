name = "کارگاه"
version = 1
is_live = False

print(name, version, is_live)

masters = ["علی ابراهیمی", "حسین کلهر", "زهرا شیرازی"]
print(masters[0])
print(len(masters))
masters.append("سارا نظری")
print(masters)

master = {
    "name": "حسین کلهر",
    "city": "تهران",
    "craft": "قالی‌بافی",
    "years_exp": 15
}
print(master["name"])
print(master.get("rating", "هنوز امتیاز ندارد"))

for m in masters:
    print(f"استاد: {m}")

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