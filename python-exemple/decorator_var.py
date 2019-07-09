from functools import wraps
from time import sleep


def delay(timer):
    def inner(fn):
        @wraps(fn)
        def wrapper():
            print("Waiting 3s before running say_hi")
            sleep(timer)
            return fn()
        return wrapper
    return inner


@delay(3)
def say_hi():
    return "hi"


print(say_hi())
