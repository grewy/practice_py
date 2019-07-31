#!/usr/bin/env python

import threading

x = 0

def increment():
    """..."""
    global x
    x += 1

def thread_task(lock):
    """..."""
    for _ in xrange(10000):
        lock.acquire()
        increment()
        lock.release()

def main_task():
    """..."""
    global x
    x = 0

    lock = threading.Lock()

    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    for idx in xrange(1, 11):
        main_task()
        print "iteration {0}: {1}".format(idx, x)
