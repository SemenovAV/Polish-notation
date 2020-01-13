class PolishNotation:
    def __init__(self, config, parser):
        self.parse = parser
        for key, value in config.items():
            setattr(self, key, value)

    def __call__(self, string):
        data = self.parse(string)
        if len(data) == 3:
            assert data[0] in dir(self), f'Ошибка: "{data[0]}" - операция не поддерживается.'
            try:
                first = int(data[1])
            except ValueError:
                raise ValueError(f'Ошибка: {data[2]} - не число')
            else:
                try:
                    second = int(data[2])
                except ValueError as e:
                    raise ValueError(f'Ошибка: {data[2]} - не число')
                else:
                    try:
                        result = getattr(self, data[0])(first, second)
                    except Exception as e:
                        raise Exception(f'Ошибка: {e}')

                    else:
                        return result
        else:
            raise ValueError(f'Ошибка: Недостаточное количество аргументов.')
