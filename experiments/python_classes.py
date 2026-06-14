class Master:
    def __init__(self, name, city, craft):
        self.name = name
        self.city = city
        self.craft = craft
        self.sessions = []

    def describe(self):
        return f"{self.name} — استاد {self.craft} از {self.city}"

    def add_session(self, session_type, price):
        self.sessions.append({"type": session_type, "price": price})

hossein = Master("حسین کلهر", "تهران", "قالی‌بافی")
hossein.add_session("studio", "500,000 تومان")
hossein.add_session("سیار", "800,000 تومان")

print(hossein.describe())
print(hossein.sessions)