
import time


def logging(func):
    def wrapper():
        print(f'{func.__name__} started')
        start = time.time()
        result = func()
        end = time.time()
        print(f'{func.__name__} took {int(end - start) * 1000} ms')
        return result
    return wrapper


@logging
def neka_funkcija():
    time.sleep(1)
    return 333

neka_funkcija()