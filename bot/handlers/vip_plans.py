from aiogram import types
from bot.bot import dp

@dp.message_handler(text="💎 VIP Plans")
async def vip_plans(message: types.Message):
    await message.answer(
        "💎 <b>Crypto Elite Premium Plans</b>\n\n"
        "🔥 <b>Starter – $19/month</b>\n"
        "• 3–7 daily signals\n"
        "• Beginner trading course\n"
        "• Public support\n\n"
        
        "⚡ <b>Pro – $49/month</b>\n"
        "• Everything in Starter\n"
        "• Higher accuracy signals\n"
        "• Auto-alert bot\n"
        "• Technical analysis tool\n\n"
        
        "🚀 <b>VIP – $99/month</b>\n"
        "• Everything in Pro\n"
        "• 24/7 private support\n"
        "• Advanced MT4/MT5 EA\n"
        "• Weekly analysis + long-term signals\n\n"
        
        "👑 <b>ULTRA – $199 lifetime</b>\n"
        "• Everything in VIP for life\n"
        "• Refund guarantee if no 20% profit\n"
        "• Weekly live sessions\n"
        "• Exclusive pre-market signals\n\n"
        
        "To subscribe, send:\n👉 <b>Subscribe</b>",
        parse_mode="HTML"
    )
