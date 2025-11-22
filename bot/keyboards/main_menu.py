from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(
        KeyboardButton("💎 VIP Plans"),
        KeyboardButton("📈 Free Signals")
    )
    menu.add(
        KeyboardButton("🛠 Tools & Indicators"),
        KeyboardButton("🎓 Academy Courses")
    )
    menu.add(
        KeyboardButton("👤 My Account"),
        KeyboardButton("📞 Support")
    )
    return menu
