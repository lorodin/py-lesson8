# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен
# извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

import re


class InvalidDateError(Exception):
    message: str

    def __init__(self, message):
        super().__init__()
        self.message = message


class CustomDate:
    date_str: str

    def __init__(self, date):
        self.date_str = date

    @staticmethod
    def validate_date(year, month, day):
        if year < 0:
            raise InvalidDateError(f'Invalid year (must positive integer): {year}')
        if month <= 0 or month >= 12:
            raise InvalidDateError(f'Invalid month (1...12): {month}')
        days_on_month = [31, 29 if year % 4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if day > days_on_month[month - 1] or day < 1:
            raise InvalidDateError(f'Invalid day (1...{days_on_month[month - 1]}): {day}')

    @classmethod
    def str_date_to_int(cls, str_date):
        cc = cls(str_date)
        res = re.findall(r'^(\d+)-(\d+)-(\d+)$', cc.date_str)

        if len(res) == 0:
            raise InvalidDateError(f'Date must be YYYY-MM-DD: {str_date}')

        year, month, day = int(res[0][0]), int(res[0][1]), int(res[0][2])
        CustomDate.validate_date(year, month, day)

        return year, month, day


if __name__ == "__main__":
    example_dates = [
        {
            'date': '2021-1-1',
            'valid': True
        },
        {
            'date': '2020-2-29',
            'valid': True
        },
        {
            'date': '2021-2-29',
            'valid': False
        },
        {
            'date': '---',
            'valid': False
        }
    ]

    for date in example_dates:
        try:
            int_dates = CustomDate.str_date_to_int(date['date'])
            if date['valid']:
                print(f'Validate success: '
                      f'Date {date["date"]} is valid. '
                      f'Year: {int_dates[0]}, Month: {int_dates[1]}, Day: {int_dates[2]}')
            else:
                print(f'Error. Date {date["date"]} must be invalid')
        except InvalidDateError as date_error:
            if date['valid']:
                print(f'Error. Date {date["date"]} is valid')
            else:
                print(f'Validate success. Date {date["date"]} is invalid')
