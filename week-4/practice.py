def get_val():
    while True:
        try:
            inp = int(input('Unesite broj: '))
        except Exception as e:
            print('Niste unjeli broj')
        else:
            print('Broj je')
        finally:
            print('Finally block')

def build_quadratic(a, b, c):
    return lambda x: a * x** 2 + b * x + c

f = build_quadratic(1,2,3)
print(f(1))

l = [1, 2, 3, 4, 5, 6]
a = filter(lambda x: x % 2 == 0, l)
print(*a)

a = [5, 4, 3, 2]
b = [2, 3, 4, 3]

c = list(map(lambda x, y: x + y, a, b))
print(c)

from functools import reduce

a = [('Podgorica', 15), ('Moscow', 5), ('Vashington', 10)]
s = reduce(lambda x, y: x + y, map(lambda x: x[1], a))
print(s)

a = [1,2,3]
b = [4,5,6]
c = zip(a, b)
print(*c)