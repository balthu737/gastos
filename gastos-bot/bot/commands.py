def handle_text(user_id, text):
    texto = text
    texto = texto.lower()
    texto = texto.strip()
    texto = texto.split()
    if not "gasto" == texto[0]:
        return "/help"
    else:
        return "Gasto detextado"
    return "Texto procesado correctamente"

