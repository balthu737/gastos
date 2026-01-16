try:
    import telebot
    print("se importo de forma correcta")
except ModuleNotFoundError as e:
    print(e)
token = "8017156472:AAFQbaQNjtlhS2KCe9W_4-MxCR-2Wm9CKRc"
def boti(token, funcion):
    toke = token
    bot = telebot.TeleBot(toke)
    @bot.message_handler(func=lambda message: True)
    def guardar_mensaje(message):
        mensaje = message.text
        funcion(mensaje)
    bot.polling(non_stop=True)

