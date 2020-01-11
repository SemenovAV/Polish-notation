class PolishNotation:
    def __init__(self, config, parser):
        self.parse = parser
        for key, value in config.items():
            setattr(self, key, value)

    def __call__(self, string):
        data = self.parse(string)
        return getattr(self, data[0])(int(data[1]), int(data[2]))
