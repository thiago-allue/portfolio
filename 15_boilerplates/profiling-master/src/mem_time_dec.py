import os
import time
import json

import psutil


def elapsed_since(start):
    return time.strftime("%H:%M:%S", time.gmtime(time.time() - start))


def get_process_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss


def track(func):
    def wrapper(*args, **kwargs):
        mem_before = get_process_memory() / 1024 ** 2
        start = time.time()
        result = func(*args, **kwargs)
        elapsed_time = elapsed_since(start)
        mem_after = get_process_memory() / 1024 ** 2

        metrics = {
            'callable': func.__name__,
            'memory_before': mem_before,
            'memory_after': mem_after,
            'memory_used': mem_after - mem_before,
            'exec_time': elapsed_time
        }
        print(f"{json.dumps(metrics, indent=4)}")
        return result

    return wrapper


@track
def create_list(n):
    print("inside list create")
    return [1] * n


def main():
    create_list(int(1e9))


if __name__ == '__main__':
    main()
    input()
