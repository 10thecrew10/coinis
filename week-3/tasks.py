import re


def task1(text: str, word: str):
    sentences = re.split(r'[.!?]', text)
    if sentences[-1] == '':
        sentences.pop(-1)
    res = []
    for s in sentences:
        temp = []
        for w in s.split():
            if w.endswith(word):
                temp.append(w)
        temp.append(len(temp))
        res.append(tuple(temp))
    return res


print(task1('Print only the words that letter in those sentences. Example can contains one or more sentences.', 's'))


def task2(l: list):
    val = max(set(l), key=lambda x: l.count(x) * x)
    return [val] * l.count(val), val ** l.count(val)


print(task2([1, 2, 2, 3, 3, 4, 4]))


def task3(text: str):
    max_len = 0
    start_position = None
    curr_len = 0
    start_flag = False
    for i in range(len(text) - 1):
        if text[i].isdigit() and not start_flag:
            curr_len = 1
            start_flag = True
        if start_flag and text[i + 1].isdigit() and text[i + 1] > text[i]:
            curr_len += 1
            if max_len < curr_len:
                start_position = i + 1 - max_len
                max_len = curr_len
        else:
            start_flag = False
    return text[start_position: start_position + max_len]


print(task3('012340123fk94123456789567'))


def task4(text: str):
    return sum(1 for i in range(len(text) - 1) if text[i] == text[i + 1])


print(task4('aabaaac'))


def task5(l: list):
    found = max(l, key=lambda x: x['br_negativni'] / (x['br_pozitivni'] + x['br_negativni']))
    if found:
        return found['naziv']


test_data = [{'naziv': 'Español para principiantes', 'br_pozitivni': 1000, 'br_negativni': 10},
             {'naziv': 'Philophize This!', 'br_pozitivni': 500, 'br_negativni': 30},
             {'naziv': 'Science VS. ', 'br_pozitivni': 600, 'br_negativni': 45}]

print(task5(test_data))
