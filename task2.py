# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class CustomZeroDivisionError(Exception):
    pass


def div(a, b):
    if b == 0:
        raise CustomZeroDivisionError
    return a / b


if __name__ == "__main__":
    try:
        a = int(input("Input A: "))
        b = int(input("Input B: "))
        print(f'{a} / {b} = {div(a, b)}')
    except CustomZeroDivisionError as error:
        print('Div by zero')
    except ValueError:
        print('Invalid values')
