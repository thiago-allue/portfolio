import time
import logging
from functools import wraps

logging.basicConfig()
log = logging.getLogger(__name__)


def retry(f):
    @wraps(f)
    def wrapped_f(*args, **kwargs):
        max_attempts = 5
        for attempt in range(1, max_attempts + 1):
            try:
                return f(*args, **kwargs)
            except:
                log.exception(
                    'Attempt %s/%s failed : %s', attempt, max_attempts, (args, kwargs)
                )
                time.sleep(2 * attempt)
        log.critical('All %s attempts failed : %s', max_attempts, (args, kwargs))

    return wrapped_f


counter = 0


@retry
def something_to_retry(arg):
    global counter
    counter += 1
    # This will throw an exception in the first 2 calls
    # And will work fine in the 3rd call
    if counter < 3:
        raise ValueError(arg)

    print('Success!')


if __name__ == '__main__':
    something_to_retry('invalid value')
