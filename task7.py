# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
# умножение созданных экземпляров. Проверьте корректность полученного результата.
#

class Complex:
    d: float
    i: float

    def __init__(self, d = 0, i = 0):
        self.d = d
        self.i = i

    def __add__(self, other):
        return Complex(self.d + other.d, self.i + other.i)

    def __mul__(self, other):
        return Complex(
            self.d * other.d - self.i * other.i,
            self.d * other.i + self.i * other.d
        )

    def __str__(self):
        return f'{self.d}+{self.i}i'


if __name__ == '__main__':
    c1 = Complex(2, 1)
    c2 = Complex(3, 4)
    s = c1 + c2
    print(f'({c1}) + ({c2}) = {s}')
    if s.d != 5 or s.i != 5:
        print('Error. Sum is incorrect')

    m = c1 * c2
    print(f'({c1}) * ({c2}) = {m}')
    if m.d != 2 or m.i != 11:
        print('Error. Mul is incorrect')
