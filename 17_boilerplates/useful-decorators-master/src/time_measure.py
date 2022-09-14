import time
from functools import wraps


def measure(func):
    @wraps
    def wrapped():
        start_time = time.time()
        func()
        time.time() - start_time

    return wrapped
