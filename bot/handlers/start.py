from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from bot.bot import dp
from bot.keyboards.main_menu import main_menu


@dp.message_handler(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        "👋 Welcome to <b>Crypto Elite</b>\n"
        "Your premium system for VIP signals, auto-trading tools, and smart portfolio growth.\n\n"
        "Choose an option below:",
        reply_markup=main_menu()
    )
