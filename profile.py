"""
https://stackoverflow.com/questions/5375624/a-decorator-that-profiles-a-method-call-and-logs-the-profiling-result
"""

import cProfile
import functools
import logging
import time

logging.basicConfig(level=logging.INFO)

def profileit(func):
    @functools.wraps(func)  # <-- Changes here.
    def wrapper(*args, **kwargs):
        datafn = func.__name__ + ".profile" # Name the data file sensibly
        prof = cProfile.Profile()
        retval = prof.runcall(func, *args, **kwargs)
        prof.dump_stats(datafn)
        return retval
    return wrapper


def profile(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        started_at = time.clock()
        result = func(*args, **kwargs)
        logging.info("%f" % (time.clock() - started_at))
        return result
    return wrap
