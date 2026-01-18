from config import TELEGRAM_BOT_TOKEN
from bot.telegram_bot import boti
from services.expense_service import message_handler
from database.db import conexion
from database.expense_repository import create_table, insert_expense, get_all_expenses

token = TELEGRAM_BOT_TOKEN
def handler(text):
    return message_handler(text, insert_expense)
conexion()
create_table()
boti(token, handler)