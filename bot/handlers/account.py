from aiogram import types
from bot.bot import dp

@dp.message_handler(text="👤 My Account")
async def my_account(message: types.Message):
    await message.answer(
        "👤 <b>Your Account</b>\n\n"
        f"• Name: <i>{message.from_user.full_name}</i>\n"
        "• Subscription: <b>None</b>\n"
        "• Expiration: <i>No active plan</i>\n\n"
        "⚡ You can upgrade anytime from the VIP Plans section.",
        parse_mode="HTML"
    )
