import math


def task1(a: int, b: int):
    return (a * b, (a + b) * 2)


def task2(a: float, b: float, c: float):
    d = b ** 2 - 4 * a * c
    if d == 0:
        return (-b / (2 * a))
    elif d > 0:
        return ((-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a))


def task3(a: int, b: int):
    return a ** 2 - b ** 2


def task4(d: int, s: int):
    return 2 * (d + s) * 4


def task5(d: int, s: int):
    return (d / 100) * (s / 100)


def task6(a: int, b: int, c: int):
    return (a + b + c ) ** 2


def task7(hours: int, ):
    return math.floor(hours / 2)


def task8(p: float):
    r = (p / math.pi) ** 0.5
    return 2 * math.pi * r


def task9(d: int, s: int, r: int):
    return (d + s + 2 * r) * 2


def task10(x1: int, y1: int, x2: int, y2: int):
    a = max(x2, x1) - min(x2, x1)
    b = max(y2, y1) - min(y2, y1)
    return (a * b, 2 * (a + b))