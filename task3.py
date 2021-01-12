# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не
# остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и
# отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

STOP_KEY = 'stop'


class NotNumberException(Exception):
    message: str

    def __init__(self, value):
        self.message = f'Error: `{value}` is not number'


class ListWrapper:
    data: list

    def __init__(self, lst: list):
        self.data = lst

    def put_item(self, value):
        try:
            self.data.append(float(value))
        except ValueError:
            raise NotNumberException(value)


if __name__ == '__main__':
    data = []

    lst_wrapper = ListWrapper(data)

    while True:
        item = input('Input number (or "stop" for exit): ')
        if item == STOP_KEY:
            break
        try:
            lst_wrapper.put_item(item)
        except NotNumberException as error:
            print(error.message)

    print('Result list: ', data)
