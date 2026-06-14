def search_masters(masters_list, city, craft):
    result = []
    for master in masters_list:
        if (city is None or master["city"] == city) and \
           (craft is None or master["craft"] == craft):
            result.append(master)
    return result

masters = [
    {"name": "حسین", "city": "تهران", "craft": "قالی‌بافی"},
    {"name": "زهرا", "city": "اصفهان", "craft": "نگارگری"},
    {"name": "علی", "city": "تهران", "craft": "نگارگری"},
]

print(search_masters(masters, "تهران", None))
print(search_masters(masters, None, "نگارگری"))
print(search_masters(masters, "تهران", "نگارگری"))