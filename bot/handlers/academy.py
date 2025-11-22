from aiogram import types
from bot.bot import dp

@dp.message_handler(text="🎓 Academy Courses")
async def academy_courses(message: types.Message):
    await message.answer(
        "🎓 <b>Crypto Elite Academy</b>\n"
        "Educational content for all levels.\n\n"

        "📘 <b>Beginner Trading Course</b>\n"
        "• Introduction to Crypto & Forex\n"
        "• How trading works\n"
        "• Risk management basics\n"
        "Status: <i>Coming soon...</i>\n\n"

        "📙 <b>Advanced Trading Course</b>\n"
        "• Price action techniques\n"
        "• Liquidity zones & smart money concepts\n"
        "• Strategy building\n"
        "Status: <i>Coming soon...</i>\n\n"

        "📗 <b>Trading Psychology Course</b>\n"
        "• Emotions in trading\n"
        "• Discipline and consistency\n"
        "Status: <i>Coming soon...</i>\n\n"

        "📕 <b>PDF Training Pack</b>\n"
        "• Cheat sheets\n"
        "• Strategy breakdowns\n"
        "Status: <i>Coming soon...</i>\n\n"

        "🔥 Courses will unlock based on your plan.\n",
        parse_mode="HTML"
    )
