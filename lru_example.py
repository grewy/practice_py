try:
    from functools import lru_cache
except ImportError:
    from backports.functools_lru_cache import lru_cache
from datetime import datetime

@lru_cache(maxsize=None)
def fib_cache(n):
    if n < 2:
        return n
    return fib_cache(n-1) + fib_cache(n-2)

def fib_no_cache(n):
    if n < 2:
        return n
    return fib_no_cache(n-1) + fib_no_cache(n-2)

def timeit(func,samples):
    start = datetime.now()
    func(samples)
    end = datetime.now()
    return end-start


print(timeit(fib_cache, 1000))
#print(timeit(fib_no_cache, 50))
