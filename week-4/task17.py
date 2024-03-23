from typing import Callable
import time
import timeit


def measure_time(func: Callable):
    def wrapper():
        start_time = time.time()
        res = func()
        res1 = (time.time() - start_time) * 1000
        print(f'Measured time for function "{func.__name__}": %.2fms' % res1, end=' | ')
        res2 = timeit.timeit(func, number=1) * 1000
        print('Timeit result: %.2fms' % res2, end=' | ')
        print('Delta: %.2fms' % (res2 - res1))
        return res

    return wrapper


@measure_time
def f1():
    a = 0
    for i in range(1024):
        a += 2 ** 10000


@measure_time
def f2():
    a = 0
    for i in range(2048):
        a += 2 ** 10000


@measure_time
def f3():
    a = 0
    for i in range(4096):
        a += 2 ** 10000

f1()
f2()
f3()