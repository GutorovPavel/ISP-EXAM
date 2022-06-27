import logging
import random

logging.basicConfig(
    level=logging.DEBUG,
    filename="mylog.log"
)


def param_decorator(*args):
    def decorator(func):
        def wrapper():
            try:
                return func()
            except args:
                logging.exception("Exception")

        return wrapper
    return decorator


@param_decorator(TimeoutError, RuntimeError)
def test_f():
    value = random.randint(1, 4)

    print(value)

    if value == 1:
        raise TimeoutError
    if value == 2:
        raise ConnectionError
    if value == 3:
        raise RuntimeError
    if value == 4:
        raise InterruptedError
    if value == 0:
        return 1

    print("I am alive")


test_f()
