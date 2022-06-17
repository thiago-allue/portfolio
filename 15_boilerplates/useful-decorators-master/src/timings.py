import os
import time
from functools import wraps


def timing(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time()
        print(
            'Processing: %r With args: [%r, %r] Took: %2.4f seconds'
            % (f.__name__, args, kwargs, end_time - start_time)
        )
        return result

    return wrap


@timing
def func():
    time.sleep(3)


def main():
    func()


if __name__ == '__main__':
    print(os.path.abspath(os.path.dirname(__name__)))
    main()
