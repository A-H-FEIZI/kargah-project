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