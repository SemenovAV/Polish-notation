from lib.polishNotation import PolishNotation
from config.config import config
from function.parse import parse

pn = PolishNotation(config, parse)

pn.__doc__ = """
        Реализация польской нотации для двух чисел и четырех операций:
        "+" - сложение,
        "-" - вычитание,
        "*" - умножение,
        "/" - денление.
        Введите знак операции и два числа через пробел, пример:
        "+ 2 2"
        Для выхода введите: exit
        Чтобы увидеть это сообщение введите: help
    """
