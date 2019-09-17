
import multiprocessing
import time

q = multiprocessing.Queue(5)
print(q)


def producer():
    while True:
        if not q.full():
