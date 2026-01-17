try:
    import telebot
    print("se importo de forma correcta")
except ModuleNotFoundError as e:
    print(e)
from .commands import Commnads

def boti(token, funcion):
    toke = token
    bot = telebot.TeleBot(toke)
    commands = Commnads()
    @bot.message_handler(commands=["start"])
    def start_handler(message):
        response = commands.start()
        bot.reply_to(message, response)
    @bot.message_handler(commands=["help"])
    def help_hamdler(message):
        responde = commands.help()
        bot.reply_to(message, responde)
    @bot.message_handler(func=lambda message: True)
    def guardar_mensaje(message):
        mensaje = message.text
        funcion(mensaje)
    bot.polling(non_stop=True)

