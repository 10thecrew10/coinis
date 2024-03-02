from task_11_20 import task19


def task31(d: float = 50):
    x = (d ** 2 / (16 ** 2 + 9 ** 2)) ** 0.5
    return (16 * x) * (9 * x)


def task32(n: int):
    arr = list(map(int, str(n)))
    return arr[0] * arr[2] + 2 + arr[5] == arr[1] + arr[3] * arr[4]


def task33(square_side, d, s):
    return (d // square_side) * (s // square_side)


def task34(n: int):
    sum_n = task19(n)
    product = task19(int(str(n)[2:4]), action='product')
    return sum_n - product


def task35(n: int):
    return n % 10 + n // 100 % 10
