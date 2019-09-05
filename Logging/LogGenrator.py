import logging as log
from time import time, sleep
import random
from threading import Thread

print(dir(log))

LogFile = 'log.txt'
LogFileMode = 'a+'
LogLevel = log.INFO

logger = log.getLogger('ThreadLogger')
logger.setLevel(log.DEBUG)

format = '%(asctime)s %(levelname)s %(message)s'

formatter = log.Formatter(format)

handler = log.FileHandler(filename='log.txt', mode=LogFileMode)
handler.setLevel(log.DEBUG)
handler.setFormatter(formatter)

logger.addHandler(handler)


def log_generator():
    counter = 0
    while True:
        counter += 1
        logger.debug("Dummy Data Line %d" % counter)
        t = time()
        random.seed(t)
        r = random.random() * 6
        if r < 1:
            logger.debug("Going to sleep for %f s" % r)
        elif r < 2:
            logger.info("Going to sleep for %f s" % r)
        elif r < 3:
            logger.warning("Going to sleep for %f s" % r)
        elif r < 4:
            logger.error("Going to sleep for %f s" % r)
        else:
            logger.critical("Going to sleep for %f s" % r)
        sleep(r)


def main():
    while True:
        t1 = Thread(target=log_generator(), args=None)
        t1.start()
        t1.join()


if __name__ == '__main__':
    main()
    #log_generator()