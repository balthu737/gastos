def message_handler(text):
    texto = text.lower().strip().split()
    if not texto:
        return "Formato inválido"
    if len(texto) < 3:
        return "Formato inválido: gasto <monto> <categoria>"
    if texto[0] != "gasto":
        return "El comando debe empezar con 'gasto'"
    if not texto[1].isnumeric():
        return "El monto debe ser un número"
    monto = int(texto[1])
    categoria = texto[2]
    print(f"Gasto registrado: {monto} en {categoria}")