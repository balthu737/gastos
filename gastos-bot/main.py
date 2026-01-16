from config import TELEGRAM_BOT_TOKEN
from bot.telegram_bot import boti
from bot.commands import handle_text
token = TELEGRAM_BOT_TOKEN
boti(token, handle_text)