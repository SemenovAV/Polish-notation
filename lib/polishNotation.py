class PolishNotation:
    def __init__(self, config, parser):
        self.parse = parser
        for key, value in config.items():
            setattr(self, key, value)

    def __call__(self, string):
        data = self.parse(string)
        if data[0] in dir(self):
            try:
                first = int(data[1])
            except ValueError:
                print(f'Ошибка: {data[1]} - не число')
            else:
                try:
                    second = int(data[2])
                except ValueError as e:
                    print(f'Ошибка: {data[2]} - не число')
                else:
                    try:
                        result = getattr(self, data[0])(first, second)
                    except Exception as e:
                        return f'Ошибка: {e}'

                    else:
                        return result
        else:
            return f'Ошибка: "{data[0]}" - операция не поддерживается.'
