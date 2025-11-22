from aiogram import types
from bot.bot import dp

@dp.message_handler(text="🛠 Tools & Indicators")
async def tools_menu(message: types.Message):
    await message.answer(
        "🛠 <b>Crypto Elite — Tools & Indicators</b>\n"
        "These tools will be activated based on your subscription plan.\n\n"

        "🔧 <b>AI Trend Scanner</b>\n"
        "• Detects market direction using smart algorithms.\n"
        "• Status: <i>Coming soon...</i>\n\n"

        "📡 <b>Auto-Alert Bot</b>\n"
        "• Sends alerts based on key price movements.\n"
        "• Status: <i>Coming soon...</i>\n\n"

        "📊 <b>TradingView Indicators</b>\n"
        "• Smart Entry Indicator\n"
        "• Volume HeatMap\n"
        "• DZ Trend Catcher\n"
        "• Status: <i>Coming soon...</i>\n\n"

        "🤖 <b>Auto-Trading Bot</b>\n"
        "• Connects to your exchange and automates trades.\n"
        "• Status: <i>Coming soon...</i>\n\n"

        "📈 <b>Market Analyzer</b>\n"
        "• Shows strongest pairs & volatility ranking.\n"
        "• Status: <i>Coming soon...</i>\n\n"

        "🔥 All tools will be fully available in VIP & ULTRA plans.\n",
        parse_mode="HTML"
    )
