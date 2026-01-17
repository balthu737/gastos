try:
    import telebot
    print("se importo de forma correcta")
except ModuleNotFoundError as e:
    print(e)
class Commnads():
    def start(self):
        return """
Hola! iniciaste balthu bot, este bot va a ser tu asistente personal.
Si quere saber como se usa toca aca --> /help
    """
    def help(self):
        return"""
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
/anio
    devuelve el total gastado en el año y en que cateforias.
    """
