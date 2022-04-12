""" Examples of decorators to perform simple memory profiling. """

import os
import time
import inspect
import datetime
import functools
import logging
import logging.config

import pandas as pd
import psutil

# Logging configuration
log_config = {
    'version': 1,
    'formatters': {
        'detailed': {
            'format': (
                '[%(asctime)s] - %(levelname)s - [%(filename)s:%(funcName)s:%(lineno)d]'
                ' - [%(process)d:%(processName)s | %(thread)d:%(threadName)s] - %(message)s'
            ),
        },
        'timer_fmt': {
            'format': '%(asctime)s,%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'detailed',
            'level': 'INFO',
        },
        'logfile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'detailed',
            'filename': '{}.log'.format(
                datetime.datetime.utcnow().strftime('%Y-%m-%d')
            ),
            'mode': 'w',
        },
        'timer_handler': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'timer_fmt',
            'filename': 'timer.csv',
            'mode': 'a',
        },
    },
    'loggers': {
        '': {'handlers': ['logfile', 'console'], 'level': 'DEBUG'},
        'timer_logger': {'handlers': ['timer_handler', 'console'], 'level': 'INFO',},
    },
}

logging.config.dictConfig(log_config)
timer_logger = logging.getLogger('timer_logger')

# Initializing global
performance_df = pd.DataFrame(
    columns=['timestamp', 'callable_', 'memory_diff', 'total_memory', 'description']
)


def timing(f):
    """
    Simple quick decorator to take time measurements.
    """

    @functools.wraps(f)
    def wrap(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time()
        msg = 'Processing: {} With args: [{}, {}] Took: {:2.4f} seconds'.format(
            f.__name__, args, kwargs, end_time - start_time
        )
        timer_logger.info(end_time - start_time)
        return result

    return wrap


def memory(f):
    """
    Decorator that appends metrics of memory to a global data frame and 
    saves it into a file for additional analysis.
    """

    @functools.wraps(f)
    def wrap(*args, **kwargs):
        global performance_df
        start_memory = psutil.Process(os.getpid()).memory_info().rss / 1024.0 / 1024.0
        result = f(*args, **kwargs)
        end_memory = psutil.Process(os.getpid()).memory_info().rss / 1024.0 / 1024.0
        performance_df = performance_df.append(
            dict(
                timestamp=datetime.datetime.utcnow().isoformat(),
                callable_=f.__name__,
                memory_diff=end_memory - start_memory,
                total_memory=end_memory,
            ),
            ignore_index=True,
        )
        performance_df.to_csv('metrics.csv')
        return result

    return wrap


class Memory:
    """
    Class decorator
    """

    def __init__(self, msg='Memory'):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor
        """
        self.msg = msg

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process. You can only give
        it a single argument, which is the function object.
        """

        def wrapped_f(*args, **kwargs):
            global performance_df
            start_memory = (
                psutil.Process(os.getpid()).memory_info().rss / 1024.0 / 1024.0
            )
            result = f(*args, **kwargs)
            end_memory = psutil.Process(os.getpid()).memory_info().rss / 1024.0 / 1024.0
            performance_df = performance_df.append(
                dict(
                    timestamp=datetime.datetime.utcnow().isoformat(),
                    callable_=f.__name__,
                    memory_diff=end_memory - start_memory,
                    total_memory=end_memory,
                    description=self.msg,
                ),
                ignore_index=True,
            )
            performance_df.to_csv('class_memory_decorator.csv')
            return result

        return wrapped_f


def measure_memory(msg):
    """
    Function to be used to manually take measurements of memory usage 
    across the execution and implementation.

    Parameters
    ----------
    msg: str
         Optional, provides an additional text for further analysis or identification
    """
    global performance_df
    try:
        pid = os.getpid()
        process = psutil.Process(pid)
        if msg:
            logging.info(msg)
        memory = process.memory_info().rss / 1024.0 / 1024.0
        logging.info('Memory {} MB'.format(memory))

        try:
            callee = inspect.stack()[1].function
        except:
            callee = ''

        performance_df = performance_df.append(
            dict(
                timestamp=datetime.datetime.utcnow().isoformat(),
                total_memory=memory,
                callable_=callee,
                description=msg,
            ),
            ignore_index=True,
        )
        performance_df.to_csv('measure_memory.csv')
    except Exception as e:
        logging.exception(e)
