from task_11_20 import task11
import math


def task21(n: int):
    a1 = n // 1000
    b1 = n % 10

    a2 = n // 100 % 10
    b2 = n // 10 % 10

    return (a1 + b1) ** 2 - (a2**2 - b2**2)


def task22(n: int, k: int, p1: float, p2: float):
    total = (n - k) * p1 + k * p2
    return '%.2f' % (total / n)


def task23(a: int, b: int):
    return (a + b) / 2


def task24(x: int, y: int):
    return f'x={y} i y={x}.'


def task25(distance: float):
    return math.floor(abs(distance / 100))


def task26(number: int):
    return number // 10 % 10


def task27(number: int):
    return sum(int(x) for x in str(number) if x.isdigit()) ** 2


def task28(number: int):
    return int(str(number)[::-1])


def task29(x1: int, y1: int, x2: int, y2: int):
    distance = task11(x1, y1, x2, y2) / 2
    point_c = ((x1 + x2) / 2, (y1 + y2) / 2)
    return point_c, distance


def task30():
    return (543 // 63) * (130 // 63)
