class PolishNotation:
    def __init__(self, config, parser):
        self.parse = parser
        for key, value in config.items():
            setattr(self, key, value)

    def __call__(self, string):
        data = self.parse(string)
        length = len(data)
        if length < 3:
            raise ValueError('Недостаточное количество аргументов.')
        elif length > 3:
            print(F'Количество аргументов больше трех! Лишнее откинуты')
        assert data[0] in dir(self), f'"{data[0]}" - операция не поддерживается.'
        arg = None
        try:
            arg = data[1]
            first = int(data[1])
            arg = data[2]
            second = int(data[2])
            arg = None
            result = getattr(self, data[0])(first, second)
        except ValueError:
            raise ValueError(f'Аргумент "{arg}" - не число')
        except ZeroDivisionError:
            raise ValueError('На ноль делить нельзя')
        else:
            return f'Результат операции: {result}'
