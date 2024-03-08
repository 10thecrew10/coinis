from dataclasses import dataclass


def task1(x: int):
    if x % 2:
        print('Portal ostaje zatvoren')
        return
    print('Portal se otvara!')


def task2(p: int, m: int):
    if p > m:
        print('Petar')
        return
    print('Milos')


def task3(p: int, passed: bool):
    if p >= 75 and passed:
        print('Dozvoljeno')
        return
    print('Nije dozvoljeno')


def task4(h: int):
    if 22 <= h <= 6 or 13 <= h <= 17:
        print('Nije moze')
        return
    print('Moze')


def task5(a: float, b: float, c: float):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False


def task6(x: int, y: int):
    if 2 * x + 5 == y:
        return True
    return False


def task7(arr: list):
    return sorted(arr, key=lambda x: (x[0] + x[1], x[1]), reverse=True)

print('task7 =', task7([[50, 49], [49, 50], [1, 2]]))


def task8(p: float):
    if p >= 4.5:
        print('Odlican')
    elif p >= 3.5:
        print('VrloDobar')
    elif p >= 2.5:
        print('DobarUspjeh')
    elif p >= 2:
        print('Dovoljan')
    else:
        print('Nedovoljan')


@dataclass
class Point:
    x: float
    y: float


def task9(p1: Point, p2: Point, p3: Point, p4: Point):
    if  (p1.x <= p3.x and p1.y >= p3.y) and (p2.x >= p4.x and p2.y <= p4.y):
        return True
    return False

print('task9 =', task9(Point(-2 ,3), Point(4, -2), Point(-1 , 2), Point(3, -1)))


def task10(r, target: Point, arrow: Point):
    if r >= ((target.x - arrow.x)**2 + (target.y - arrow.y))**0.5:
        return True
    return False


def task11(p1: Point, p2: Point, ant: Point):
    if (ant.x == p1.x or ant.x == p2.x) and p1.y >= ant.y and p2.y <= ant.y:
        return True
    if (ant.y == p1.y or ant.y == p2.y) and p1.x <= ant.x and p2.x >= ant.x:
        return True

    return False

print(task11(Point(-3, 2), Point(2, -1), Point(-1, 2)))


def task12(n: int):
    first, last = n // 10, n % 10
    if first > last:
        return first - last
    elif first < last:
        return first + last
    else:
        first * last


def task13(r1: float, r2: float):
    return max(r1, r2)


def task14(p1: float, p2: float, p3: float):
    arr = sorted([p1, p2, p3])
    return arr[0], arr[1]

print(task14(5, 4, 3))


def task15(year: int):
    if year % 400 == 0 or (year % 100 and year % 4 == 0):
        print('Yes')
        return
    print('No')


def task16(p1: Point, p2: Point, p: Point):
    if p1.x <= p.x <= p2.x and p1.y >= p.y >= p2.y:
        return True
    return False


def task17(a: int, b: int):
    if max(a, b) // min(a, b) > 1:
        return True
    return False


def task18(temp: int):
    if 0 < temp < 100:
        print('Tecno')
    if temp >= 100:
        print('Gasovito')
    else:
        print('Cvrsto')


def task19(skolarina: float, average: float, nagrada: bool):
    res = None
    if average >= 4.5:
        res = skolarina * 0.6
    if nagrada:
        res = skolarina * 0.7
    if average >= 3.5:
        res = skolarina * 0.8
    if average >= 2.5:
        res = skolarina * 0.9
    else:
        res = skolarina

    return round(res)

from functools import reduce

def task20():
    n = int(input('Input number: '))
    if n % 2:
        odds = (int(x) for x in str(n) if int(x) % 2)
        return reduce(lambda x, y: x * y, odds)

    return sum(int(x) for x in str(n) if not (int(x) % 2))


def task21(x: float):
    if x <= -7:
        return -2 * x + 7/2
    if -7 < x < 1:
        return (x*x - 3*x + 5) / (x*x + 2)
    if 1 <= x <= 8:
        return (x*x + 2*x + 2) ** 0.5
    return abs(3 / x**2 - 11 * x)


def task22(x: float, y: float):
    print('Kvadrante: ', end='')
    if x >= 0 and y >= 0:
        print('1', end='')
    if x <= 0 and y >= 0:
        print('2', end='')
    if x <= 0 and y <= 0:
        print('3', end='')
    if x >= 0 and y <= 0:
        print('4')


def task24(text: str):
    if len(text) > 30:
        return text[:30] + '...'


def task25(text: str):
    return text[1:-1]


def task26():
    number = input('Input number: ')
    if len(number) == 1 or number[1].isdigit():
        return 'decimalni'

    sliced = number[:2]
    if sliced == '0b':
        return 'binarni'
    if sliced == '0o':
        return 'oktalni'
    if sliced == '0x':
        return 'heksadecimalni'


def task27(text: str):
    return len([True for x in text if x.lower() in 'eyuoai']) > 0


def task28(text: str, target: str):
    if text.rfind(target) == len(text) - len(target):
        print('Da')
        return
    print('Ne')


def task29(text: str):
    return all(True if x in '10' else False for x in text)


def task30():
    n = int(input('Input number: '))
    sum_even = sum(x for x in range(2, n + 1, 2))
    product_odds = reduce(lambda x, y: x * y, (m for m in range(1, n + 1, 2)))
    print(sum_even, product_odds)
    print(n // 2, n // 2 + 1)


def task31(start: int, end: int):
    print(sum(x**2 for x in range(start, end + 1) if x % 2 == 0 and x % 4))


def task32(a: int, b: int, divider: int):
    arr = [x for x in range(a + 1, b) if x % divider == 0]
    return sum(arr), len(arr)


def task33():
    return sum(int(x) for x in input('Input number: '))


def task34(text: str):
    return reduce(lambda x, y: x * y, (int(x) for x in text if x.isdigit()))


def task35(text: str):
    digits = ''.join(x for x in text if x.isdigit())
    if digits:
        return int(digits)


def task36(text: str):
    return ''.join('1' if x.lower() in 'eyuioa' else '0' for x in text)


def task37(text: str):
    text = text.replace('0', '')
    return sum(1 if x == '1' else -1 for x in text) > 0


def task38(text: str):
    return ''.join('0' if x.isdigit() and int(x) % 2 else '1' for x in text)


def task39(n: int):
    l = len(str(n))
    if n == sum(int(x) ** l for x in str(n)):
        print('Da')
    else:
        print('Ne')


def task40(arr: list):
    return sum(x for x in arr if x % 2 == 0 and x < 0)


def task41(arr: list, max: int):
    return len([x for x in arr if x < max])


def task42(arr: list, discount: int):
    s = sum(arr)
    return s - s * (1 - discount / 100)


def task43(l: list):
    return sum(1 for x in l if x > 2)


def task44(l: list):
    return max(l)


def task45(l: list):
    avg = sum(l) / len(l)
    return sum(1 for x in l if x > avg)


def task46(l: list):
    return sorted(l)[-2]


def task47():
    l = []
    for i in range(3):
        l.append(int(input(f'Input {i + 1} number: ')))
    print('Max:', max(l), 'Min:', min(l))


def task48(x: int, n: int):
    product = 1
    for _ in range(n):
        product *= x
    return product


def task49(text: str):
    return text[:int(input('Input number: '))] + '...'


def task50(text: str):
    return ''.join(x for x in text if x.lower() in 'eyuoia')


def task51(passw: str):
    flag_lower = any(True for x in passw if x.islower())
    flag_upper = any(True for x in passw if x.isupper())
    flag_number = any(True for x in passw if x.isdigit())
    if len(passw) >= 8 and flag_number * flag_upper * flag_lower:
        return True
    return False


def task52(a: str, pre: str, suf: str, num: int):
    return pre * num + a + suf * num


def task53(n: int):
    s = 0
    k = 1
    while n > 0:
        n -= k
        k += 1
        s += 1
    return s


def task54(text: str, pos: int):
    if pos == 0:
        return text[1] == '0'
    if pos == len(text) - 1:
        return text[-2] == '0'

    return text[pos - 1] == text[pos + 1] == '0'


def task55(h: int, o: int):
    return min(h // 2, o)


def task56(text: str):
    return text.count('-')


def task57(n: int):
    l = len(str(n))
    if n == sum(int(x) ** l for x in str(n)):
        print('Da')
    else:
        print('Ne')


def task58(text: str):
    return ''.join(x for x in text if not x.isdigit())


def task59(text: str):
    return ''.join('1' if int(x) % 2 else '0' for x in text)


def task60(s: int, e:  int):
    print(sum(x ** 2 for x in range(s, e + 1)))


def task61(text: str):
    return ''.join(x for x in text if x.isupper())


def task62(text: str):
    return text.count('0x')


from re import findall

def task63(text: str):
    return max(findall('\w+', text), key=len)


def task64(n: int):
    arr = list(map(int, str(n)))
    return max(arr) + min(arr)


def task65(d: float, n: int, s: float):
    return (d * 100 - n * s) / (n + 1)


def task66(l: list):
    if sum(1 for x in l if len(str(x)) == 2) > sum(1 for x in l if len(str(x)) == 3):
        print('Dvocifrenih')
        return
    print('Trocifrenih')


def task67(l: list):
    n = int(input('Input number: '))
    return l.count(n)


def task68(l: list, x: float):
    avg = sum(l) / len(l)
    return [m + x if m > avg else m for m in l]

print(task68([1, 2, 2, 3], 10))


def task69(l: list):
    avg = sum(l) / len(l)
    return [m * 0.9 if m > avg else m * 1.1 for m in l]


def task70(l: list):
    return sum(x ** 2 for x in l if x % 3 == 0)


def task71(l: list):
    return sum(1 for x in l if (x ** 0.5)**2 == x)


def task72(l: list):
    l2 = [x for x in l if x != 5]
    avg = sum(l2) / len(l2)
    return sum(1 for x in l2 if x > avg)


def task73(pos: int):
    arr = ['sword', 'shield', 'armor', 'coat']
    return arr[pos - 1]

print(task73(1))


def task74(l: list):
    avg = sum(l) / len(l)
    return avg * 1.1


def task75():
    l = []
    print('You started a program. Input \'exit\' to break input.')
    for i in range(1000):
        val = input(f'Input {i + 1} value of savings: ')
        if val == 'exit':
            break
        if val.isnumeric():
            l.append(int(val))
        else:
            print('Incorrect input.')
            return

    val = input('Input annual interest as a percentage (e.g. 10): ')
    if val.isnumeric():
        print('Total losses:', sum(l) * float(val) / 100)
    else:
        print('Incorrect input.')
        return


def task76(l: list, old: int, new: int):
    return [x if x != old else new for x in l]

print(task76([1,2,3,4,4], 4, 10))


def task77(l: list):
    return l == sorted(l)


def task78(l: list):
    return list(set(l))[-2]


def task79(l: list):
    return [-x for x in l]


def task80(l: list):
    return max(l) - min(l)


def task81(l: list):
    arr = [l[i + 1] - l[i] for i in range(len(l) - 1)]
    return min(arr), max(arr)


def task82():
    return