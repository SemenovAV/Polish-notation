from lib.basePN import pn

state = True
while state:
    try:
        value = input('Введите знак операции и два числа через пробел:')
        if value.strip() == 'exit':
            state = False
            break
        elif value.strip() == 'help':
            print(pn.__doc__)
        else:
            print(pn(value))
    except Exception as e:
        print(f'Ошибка: {e}')
