from datetime import datetime

def hora_atual():
    return datetime.now().strftime("%d/%m/%Y %H:%M")


def calculadora(expressao):
    return str(eval(expressao))