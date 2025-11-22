from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from bot.bot import dp
from bot.keyboards.main_menu import main_menu
from bot.utils.db import add_user


@dp.message_handler(CommandStart())
async def start_cmd(message: types.Message):
    # تسجيل المستخدم في قاعدة البيانات
    await add_user(
        message.from_user.id,
        message.from_user.full_name,
        message.from_user.username
    )

    # رسالة الترحيب + المنيو
    await message.answer(
        "👋 Welcome to <b>Crypto Elite</b>\n"
        "Your premium system for VIP signals, auto-trading tools, and smart portfolio growth.\n\n"
        "Choose an option below:",
        reply_markup=main_menu()
    )
