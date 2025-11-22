from aiogram import types
from bot.bot import dp

@dp.message_handler(text="📈 Free Signals")
async def free_signals(message: types.Message):
    await message.answer(
        "📈 <b>Free Signals</b>\n"
        "Here is a taste of our daily high-accuracy signals 👇\n\n"
        
        "🔹 <b>BTC/USDT</b>\n"
        "Entry: 43120\n"
        "TP1: 43300\n"
        "SL: 42750\n\n"
        
        "🔹 <b>ETH/USDT</b>\n"
        "Entry: 2460\n"
        "TP1: 2485\n"
        "SL: 2420\n\n"
        
        "🔥 Want full VIP signals? Upgrade anytime!",
        parse_mode="HTML"
    )
