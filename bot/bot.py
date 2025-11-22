from aiogram import Bot, Dispatcher
from bot.config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

# Load handlers
from bot.handlers import start, vip_plans, free_signals, tools, academy, account, support
