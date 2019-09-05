import logging as log
import random
from threading import Thread
from time import time, sleep

import queue
from queue import Queue

LogFile1 = 'log1.txt'
LogFile2 = 'log2.txt'

logger1 = log.getLogger('')
logger1.setLevel(log.DEBUG)

#logger2 = log.getLogger('my-logger') # If logger class is same no need to create muliple logger
#logger2.setLevel(log.ERROR)

format1 = '%(asctime)s %(filename)s **%(levelname)s** %(message)s'
datfmt1 = '%Y %m %d %H:%M:%S'
format2 = '%(asctime)s %(filename)s %(funcName)s %(process)s ***%(levelname)s*** %(message)s'
#datfmt2 = '%Y %m %d %H:%M:%S'

formatter1 = log.Formatter(format1, datefmt=datfmt1)
formatter2 = log.Formatter(format2)

handler1 = log.FileHandler(LogFile1)
handler1.setLevel(log.DEBUG)
handler1.setFormatter(formatter1)

handler2 = log.FileHandler(LogFile2)
handler2.setLevel(log.ERROR)
handler2.setFormatter(formatter2)

#handler3 = log.StreamHandler()

logger1.addHandler(handler1)
logger1.addHandler(handler2)

stoplog = False

def log_generator():
    counter = 0
    global stoplog
    while True:
        if stoplog:
            break
        counter += 1
        logger1.debug("Dummy Data Line %d" % counter)
        t = time()
        random.seed(t)
        r = random.random() * 6
        if r < 1:
            logger1.debug("Going to sleep for %f s" % r)
        elif r < 2:
            logger1.info("Going to sleep for %f s" % r)
        elif r < 3:
            logger1.warning("Going to sleep for %f s" % r)
        elif r < 4:
            logger1.error("Going to sleep for %f s" % r)
        else:
            logger1.critical("Going to sleep for %f s" % r)
        sleep(r)

def stop_log():
    pass

def main():
    while True:
        t1 = Thread(target=log_generator(), args=None)
        t1.start()
        t2 = Thread(target=stop_log(), args=None)
        t2.start()
        t1.join()
        t2.join()

if __name__ == '__main__':
    main()
