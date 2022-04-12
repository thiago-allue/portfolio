import time
import functools
# import resource  # only works on Unix
import timeit
import contextlib


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer(contextlib.ContextDecorator):
    timers = dict()

    def __init__(
        self,
        name=None,
        text="Elapsed time: {:0.4f} seconds",
        logger=print,
    ):
        self._start_time = None
        self.name = name
        self.text = text
        self.logger = logger

        # Add new named timers to dictionary of timers
        if name:
            self.timers.setdefault(name, 0)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.stop()

    def start(self):
        """ Start a new timer """
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    @property
    def elapsed(self):
        return time.perf_counter() - self._start_time

    def stop(self):
        """ Stop the timer, and report the elapsed time """
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

        if self.logger:
            self.logger(self.text.format(elapsed_time))
        if self.name:
            self.timers[self.name] += elapsed_time

        return elapsed_time


@Timer('time_function')
def another():
    time.sleep(2)


def main():
    with Timer('nameless'):
        lst = [i for i in range(100000)]
        time.sleep(3)

    another()

    with Timer('nameless') as t:
        time.sleep(3)

    with Timer('nameless') as t:
        time.sleep(3)
        print(f'measure: {t.elapsed}')
        time.sleep(4)
        print(f'measure: {t.elapsed}')
        time.sleep(1)
        print(f'measure: {t.elapsed}')

    # Stand alone
    t = Timer()
    t.start()
    time.sleep(2)
    print(f'Checkpoint: {t.elapsed}')
    time.sleep(3)
    print(f'Total Elapsed: {t.stop()}')

    print(Timer.timers['nameless'])  # cumsum of time used by 'nameless' Timer

    # Memory consumption with psutil (MB)
    import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)

    # Memory consumption with resource (MB) - Only works on Unix
    # import resource; print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)


if __name__ == '__main__':
    main()
