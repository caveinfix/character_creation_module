from math import sqrt

message = (
    'Добро пожаловать в самую лучшую программу для '
    'вычисления квадратного корня из заданного числа'
)


def CalculateSquareRoot(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def Calc(your_number):
    """Выводит сообщение."""
    if your_number >= 0:
        result = CalculateSquareRoot(your_number)
        print(f'Мы вычислили квадратный корень из введённого вами числа.'
              f'Это будет: {result}')


print(message)
Calc(25.5)
