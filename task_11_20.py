import datetime


def task11(x1: int, y1: int, x2: int, y2: int):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def task12(n: int):
    return datetime.date.today().year - n


def task13(x1: int, y1: int, x2: int, y2: int):
    a = (x2 + 2, y2 - 3)
    b = task11(x1, y1, a[0], a[1])
    c = task11(x1, y1, x2, y2) + task11(x2, y2, a[0], a[1])

    return a, b, c


def task14(size: int, parking: bool, location: str):
    parking_value = False
    if parking == 'parking ima':
        parking_value = True

    location_value = 0
    if location == 'zona 1':
        location_value = 3
    elif location == 'zona 2':
        location_value = 2
    elif location == 'zona 3':
        location_value = 3

    per_square = 1200
    fixed_costs = 1000

    location_price = location_value * 5 * size
    parking_price = parking_value * location_price * 10

    return size * per_square + location_price + parking_price + fixed_costs


def task15(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int):
    a = task11(x1, y1, x2, y2)
    b = task11(x2, y2, x3, y3)
    c = task11(x3, y3, x1, y1)

    halphed_p = (a + b + c) / 2

    return (halphed_p * (halphed_p - a) * (halphed_p - b) * (halphed_p - c)) ** 0.5


def task16(km: float):
    return 1 + km * 0.5


def task17(price: float, discount: float):
    """Diskount mora biti u procentima (napr. 20.5)"""
    return price * (100 - discount) / 100


def task18(price: float):
    return price * 1.1 * 0.9


def task19(number: int, action: str = 'sum'):
    if action == 'sum':
        return sum(int(x) for x in str(number) if x.isdigit())
    elif action == 'product':
        product = 1
        for x in (int(x) for x in str(number) if x.isdigit()):
            product *= x
        return product


def task20(number: int):
    return task19(number, 'product') - task19(number)
