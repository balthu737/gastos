from config import TELEGRAM_BOT_TOKEN
from bot.telegram_bot import boti
from services.expense_service import message_handler
token = TELEGRAM_BOT_TOKEN
boti(token, message_handler)