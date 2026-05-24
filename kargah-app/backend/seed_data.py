"""
Run once to fill the database with sample masters and sessions.
Usage:  python seed_data.py
"""
import database


def seed():
    database.init_db()
    conn = database.get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM categories")
    if cursor.fetchone()[0] > 0:
        print("Database already has data. Skipping seed.")
        conn.close()
        return

    # --- Categories ---
    categories = [
        ("Carpet Weaving", "قالی‌بافی", "🪡"),
        ("Pottery",        "سفالگری",   "🏺"),
        ("Calligraphy",    "خوشنویسی",  "✍️"),
        ("Miniature",      "نگارگری",   "🖼️"),
        ("Metalwork",      "فلزکاری",   "⚒️"),
        ("Woodcarving",    "چوب‌کاری",  "🪵"),
        ("Jewelry",        "جواهرسازی", "💍"),
        ("Traditional Cooking", "آشپزی سنتی", "🍲"),
    ]
    cursor.executemany(
        "INSERT INTO categories (name, name_fa, emoji) VALUES (?, ?, ?)",
        categories
    )

    # --- Masters ---
    masters = [
        ("Ali Rezaei",
         "Master carpet weaver with 30 years of experience. Trained in the Isfahan school, specializing in floral and medallion patterns. Offers both studio and mobile sessions.",
         "Isfahan", 1, "", "ali@example.com", 30),

        ("Maryam Hosseini",
         "Pottery artist specializing in traditional Iranian blue ceramics and turquoise glazework from Kashan. Runs weekly beginner workshops at her studio.",
         "Kashan", 2, "", "maryam@example.com", 18),

        ("Hassan Karimi",
         "Award-winning calligrapher in Nastaliq script. Offers private lessons, group workshops, and custom wedding/event calligraphy. Can travel across Tehran province.",
         "Tehran", 3, "", "hassan@example.com", 22),

        ("Fateme Ahmadi",
         "Miniature painter inspired by the Safavid school, creating detailed narrative scenes. Accepts commissions for personalized miniature portraits and gift pieces.",
         "Shiraz", 4, "", "fateme@example.com", 12),

        ("Reza Mohammadi",
         "Third-generation metalwork artisan specializing in copper engraving (qalamzani). Offers studio tours and hands-on engraving workshops for all levels.",
         "Isfahan", 5, "", "reza@example.com", 25),

        ("Sara Jafari",
         "Woodcarving artist creating geometric Khatam patterns and traditional Persian motifs. Specializes in corporate and event workshop experiences.",
         "Yazd", 6, "", "sara@example.com", 10),

        ("Ahmad Moradi",
         "Fine jewelry maker using Iranian filigree (malileh-kari) with silver and semi-precious stones. Accepts custom commissions and teaches private workshops.",
         "Tehran", 7, "", "ahmad@example.com", 15),

        ("Zahra Ebrahimi",
         "Mobile pottery teacher who brings her portable wheel and tools to your home or office. Popular for birthday parties and corporate team-building events.",
         "Tabriz", 2, "", "zahra@example.com", 8),

        ("Mohammad Bagheri",
         "Carpet restoration specialist and weaver. Focuses on antique restoration and custom tribal patterns. Teaches the art of restoration in his Bazaar workshop.",
         "Kerman", 1, "", "mohammad@example.com", 35),

        ("Leila Nazari",
         "Calligraphy and illumination (tazhib) artist. Creates custom Quran verses, poetry, and decorative panels. Offers beginner illumination courses.",
         "Mashhad", 3, "", "leila@example.com", 14),
    ]
    cursor.executemany(
        "INSERT INTO masters (name, bio, city, category_id, image_url, contact_email, years_exp) VALUES (?, ?, ?, ?, ?, ?, ?)",
        masters
    )

    # --- Sessions ---
    # type: 'studio', 'mobile', or 'commission'
    sessions = [
        # Ali Rezaei — carpet weaving
        (1, "Carpet Weaving Introduction", "Learn the basics of traditional Persian carpet weaving. Understand knot types, color planning, and pattern reading.", "studio", 3.0, "500,000–800,000 تومان", 4),
        (1, "Mobile Carpet Demo at Your Event", "Ali brings a traditional loom and demonstrates carpet weaving at your event or office. Great for cultural events.", "mobile", 2.0, "1,500,000 تومان", 20),
        (1, "Custom Carpet Commission", "Commission a handwoven carpet in your chosen size, colors, and pattern. Delivery in 3–6 months.", "commission", None, "By quote", 1),

        # Maryam Hosseini — pottery
        (2, "Beginner Pottery on the Wheel", "Your first time on a pottery wheel. Learn centering, pulling, and basic forms. All materials provided.", "studio", 2.5, "400,000–600,000 تومان", 6),
        (2, "Mobile Pottery Party", "Maryam brings her portable wheel and clay to your home. Perfect for birthday parties and family gatherings.", "mobile", 3.0, "2,000,000 تومان (group)", 8),

        # Hassan Karimi — calligraphy
        (3, "Nastaliq Calligraphy for Beginners", "Learn the fundamentals of Persian Nastaliq script. Includes reed pen, ink, and practice paper.", "studio", 2.0, "350,000 تومان", 5),
        (3, "Wedding Calligraphy Package", "Custom calligraphy for wedding invitations, name plaques, and event signage. Hassan delivers to any city.", "commission", None, "By quote", 1),
        (3, "Corporate Calligraphy Workshop", "Team building session: each participant creates their own name in Nastaliq. Hassan travels to your office.", "mobile", 2.0, "3,500,000 تومان (team)", 15),

        # Fateme Ahmadi — miniature
        (4, "Persian Miniature Workshop", "Learn the traditional techniques of Iranian miniature painting. Pigments, brushes, and bone sheet provided.", "studio", 4.0, "600,000 تومان", 3),
        (4, "Custom Miniature Portrait", "Commission a personalized miniature painting — portrait, family scene, or story illustration.", "commission", None, "1,500,000–5,000,000 تومان", 1),

        # Sara Jafari — woodcarving
        (6, "Khatam Craft Day", "Learn the ancient art of Khatam marquetry. Create a small decorative piece to take home.", "studio", 5.0, "700,000 تومان", 4),
        (6, "Company Team-Building Khatam", "Sara facilitates a guided Khatam session at your company. All materials included.", "mobile", 4.0, "4,000,000 تومان (team)", 12),

        # Zahra Ebrahimi — mobile pottery
        (8, "Home Pottery Experience", "Zahra brings everything to your home. Perfect for families, couples, or small groups wanting a hands-on clay experience.", "mobile", 2.5, "1,800,000 تومان (up to 4 people)", 4),
    ]
    cursor.executemany(
        "INSERT INTO sessions (master_id, title, description, type, duration_hr, price_range, max_people) VALUES (?, ?, ?, ?, ?, ?, ?)",
        sessions
    )

    conn.commit()
    conn.close()
    print(f"Seeded {len(categories)} categories, {len(masters)} masters, {len(sessions)} sessions.")


if __name__ == "__main__":
    seed()
