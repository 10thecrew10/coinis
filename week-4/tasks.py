from functools import reduce


def task1():
    l = ["flower", "flow", "flight"]
    return reduce(lambda x, y: x if x > y else y, l)


print('task1 =', task1())


def task2():
    a = ['Marko', 'Blazo', 'Alex', 'Milika']
    b = [7, 8, 9, 10]
    return [x for x in zip(a, b) if x[1] > 8.5]


print('task2 =', task2())


def task3():
    l = [{'ime': 'Ana', 'godine': 22, 'prosek': 9.1},
         {'ime': 'Max', 'godine': 19, 'prosek': 8.1},
         {'ime': 'Alex', 'godine': 30, 'prosek': 7.2}]
    return sorted(filter(lambda x: x['godine'] >= 21, l), key=lambda x: x['prosek'])


print('task3 =', task3())


def task4():
    a = ["Hello, World!", "Python is cool", "Functional programming rocks"]
    return reduce(lambda x, y: x + y, map(lambda x: x.count(' ') + 1, a))


print('task4 =', task4())


def task5():
    t = [('Alex', 7, 'ADIS'), ('Max', 8, 'Mikro'), ('David', 9, 'Math'), ('Lalo', 6, 'ADIS'), ('Mia', 10, 'Mikro'),
         ('Li', 10, 'Math'), ('Alex', 10, 'ADIS')]

    subj = set(map(lambda x: x[2], t))
    res = [list(filter(lambda x: x[2] == s, t)) for s in subj]
    return [{res[i][0][2]: reduce(lambda acc, item: acc + item[1], x, 0) / len(x)} for i, x in enumerate(res)]
    # return [{res[i][0][2]: sum(elem[1] for elem in x) / len(x)} for i, x in enumerate(res)]


print('task5 =', task5())


def task6():
    l = [12, 10, 14, 20, 100, 10, 5, 1, 90]
    return list(map(lambda x, y: y - x, l[:-1], l[1:]))


print('task6 =', task6())


def task7():
    l = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    return [(x, reduce(lambda acc, item: acc + int(item == x), l, 0)) for x in set(l)]


print('task7 =', task7())

import requests


def task8():
    resp = requests.get('https://raw.githubusercontent.com/StevanCakic/ORS-UDG/master/assets/rectangles.txt')
    lines = resp.text.split('\n')
    sides = []
    for line in lines:
        sides.append(tuple(map(int, line.split(','))))

    return max(x[0] * x[1] for x in sides if x[0] == x[1])


print('task8 =', task8())


def task9():
    with open('week-4/cities.txt', 'r') as f:
        lines = map(lambda x: x.replace('\n', '').split(','), f.readlines())
        return max(lines, key=lambda x: int(x[2]))[1]


print('task9 =', task9())


def task10(country: str):
    with open('week-4/population.txt', 'r') as f:
        lines = map(lambda x: x.replace('\n', '').split(','), f.readlines())
        filtered = list(filter(lambda x: x[0] == country, lines))
        return min(filtered, key=lambda x: int(x[2]))[1]


print('task10 =', task10('Poljska'))


def task11(country: str):
    with open('week-4/population.txt', 'r') as f:
        lines = map(lambda x: x.replace('\n', '').split(','), f.readlines())
        filtered = list(filter(lambda x: x[0] == country, lines))
        return sum(int(x[2]) for x in filtered)


print('task11 =', task11('Poljska'))


def task12():
    with open('week-4/numbers.txt', 'r') as f:
        lines = map(lambda x: x.replace('\n', ''), f.readlines())
        filtered = list(filter(lambda x: x.startswith('0x'), lines))
        return sum(int(x, 16) for x in filtered if int(x, 16) % 10 == 3)


print('task12 =', task12())


def task13_append_to_file(list_of_products: list):
    with open('week-4/products.csv', 'w') as f:
        for item in list_of_products:
            f.write(', '.join(list(map(str, item.values()))) + '\n')


print('task13_append_to_file =',
      task13_append_to_file([
          {'naziv': 'Televizor', 'opis': 'LG televizor 43inc', 'godina': 2019, 'kolicina': 10, 'cijena': 300},
          {'naziv': 'Televizor', 'opis': 'Samsung televizor 39inc', 'godina': 2017, 'kolicina': 5, 'cijena': 250}]))


def task13_get_products_older_than(year: int):
    with open('week-4/products.csv', 'r') as f:
        lines = map(lambda x: x.replace('\n', '').split(', '), f.readlines())
        return list(filter(lambda x: int(x[2]) >= year, lines))


print('task13_get_products_older_than =',
      task13_get_products_older_than(2018))


def task13_max_possible_revenue():
    with open('week-4/products.csv', 'r') as f:
        lines = map(lambda x: x.replace('\n', '').split(', '), f.readlines())
        return sum(int(x[3]) * int(x[4]) for x in lines)


print('task13_max_possible_revenue =',
      task13_max_possible_revenue())


def task14_append_to_file(list_of_products: list):
    with open('week-4/students.txt', 'w') as f:
        for item in list_of_products:
            f.write(','.join(list(map(str, item.values()))) + '\n')


print('task14_append_to_file =',
      task14_append_to_file([{'ime': 'Marko', 'prezime': 'Markovic', 'godina': 2, 'prosjek': 8.6},
                             {'ime': 'Boris', 'prezime': 'Boricic', 'godina': 3, 'prosjek': 7.9},
                             {'ime': 'Novak', 'prezime': 'Novovic', 'godina': 3, 'prosjek': 6.9}]))

print('task14_append_to_file =',
      task14_append_to_file([{'ime': 'Marko', 'prezime': 'Markovic', 'godina': 1, 'prosjek': 5.6},
                             {'ime': 'Boris', 'prezime': 'Boricic', 'godina': 2, 'prosjek': 9.9},
                             {'ime': 'Novak', 'prezime': 'Novovic', 'godina': 3, 'prosjek': 10}]))


def task14_get_students_with_greater_grade(year: int, grade: float):
    with open('week-4/students.txt', 'r') as f:
        lines = map(lambda x: x.replace('\n', '').split(','), f.readlines())
        return list(filter(lambda x: int(x[2]) == year and float(x[3]) >= grade, lines))


print('task14_get_students_with_greater_grade =',
      task14_get_students_with_greater_grade(3, 7.5))

print('task14_get_students_with_greater_grade =',
      task14_get_students_with_greater_grade(2, 9.9))


def task15(card_number: str):
    if not (len(card_number) == 16 and card_number.isdigit()):
        return False

    l = list(map(int, card_number))
    for i in range(1, len(l), 2):
        temp = l[i] * 2
        if temp > 9:
            l[i] = temp % 10 + temp // 10
            continue
        l[i] = temp
    return sum(l) % 10 == 0


print('task15 =', task15('1090000000000000'))
