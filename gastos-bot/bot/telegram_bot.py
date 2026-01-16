import telebot
from config import TELEGRAM_BOT_TOKEN

token = TELEGRAM_BOT_TOKEN
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Hola! iniciaste balthu bot, este bot va a ser tu asistente personal.")

@bot.message_handler(commands=["help"])
def send_help(message):
    bot.reply_to(message, """
Hola!
¿Como estas?

Esta es la forma de usar este bot:
gasto <monto> <categoria> 

Los comando que se pueden utilizar con este bot son los siguientes:
/categoria
    devuelve el total gastado en esa categoria.
/hoy
    devuelve el total gastado hoy y en que cateforias.
/semana
    devuelve el total gastado en la semana y en que cateforias.
/mes
    devuelve el total gastado en el mes y en que cateforias.
/año
    devuelve el total gastado en el año y en que cateforias.
""")

@bot.message_handler(commands=["categoria"])
def send_categoria(message):
    bot.reply_to(message, """""")

@bot.message_handler(commands=["hoy"])
def send_hoy(message):
    bot.reply_to(message, """""")

@bot.message_handler(commands=["semana"])
def send_semana(message):
    bot.reply_to(message, """""")

@bot.message_handler(commands=["mes"])
def send_mes(message):
    bot.reply_to(message, """""")

@bot.message_handler(commands=["anio"])
def send_anio(message):
    bot.reply_to(message, """""")