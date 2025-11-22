from aiogram import types
from bot.bot import dp


@dp.message_handler(lambda m: m.text == "Support")
async def support_handler(message: types.Message):
    await message.answer("🛠 Support system coming soon!")
