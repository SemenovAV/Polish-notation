class Operation:
    def __init__(self, assertion, function):
        self.assertion = assertion
        self.operation = function

    def __call__(self, *args):
        if self.assertion(args):
            return self.operation(args)
        else:
            return None
