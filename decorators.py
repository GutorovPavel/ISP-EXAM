import logging
import time
from functools import cmp_to_key


######################  Параметризованный декоратор expired_cache  #####################################################

def expired_cache(timeout):
    def decorator(func):
        func.cached = {}

        def wrapper(*args, **kwargs):
            key = tuple(sorted(args) + sorted(kwargs.items()))
            if key not in func.cached or time.time() - func.cached[key][1] > timeout:
                print("first time", key)
                func.cached[key] = func(*args, **kwargs), time.time()
            return func.cached[key][0]

        return wrapper
    return decorator


@expired_cache(0.9)
def sum1(a, b):
    return a + b


######################## Параметризованный декоратор cached с ограничением на размер ###############################


def cached(size):
    def decorator(func):
        func.cached = {}

        def wrapper(*args, **kwargs):
            key = tuple(sorted(args) + sorted(kwargs.items()))
            if key not in func.cached:
                if len(func.cached) >= size:
                    print("clearing")
                    func.cached.clear()
                print("first time", key)
                func.cached[key] = func(*args, **kwargs)
            return func.cached[key]

        return wrapper
    return decorator


@cached(2)
def sum2(a, b):
    return a + b


##########################  Параметризованный декоратор (сортировка аргументов) ############################


def cmp(a, b):
    if a > b:
        return 1
    elif b > a:
        return -1
    else:
        return 0


def cmp_cached(cmp):
    if type(cmp) != type(cached):
        raise ValueError("cmp should be a func")

    def decorator(func):
        def wrapper(*args, **kwargs):
            args = tuple(sorted(args, key=cmp_to_key(cmp)))
            return func(*args, **kwargs)

        return wrapper
    return decorator


@cmp_cached(cmp)
def sum3(a, b, c):
    return a * 100 + b * 10 + c


def param_decorator(*args):
    def decorator(func):
        def wrapper():
            try:
                return func()
            except args:
                logging.exception("Exception")

        return wrapper
    return decorator
