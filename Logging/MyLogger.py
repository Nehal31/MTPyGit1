
import logging as log
from time import time, sleep, ctime
import datetime
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

handler = log.FileHandler('log.txt')
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
        r = random.random() * 2
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

def logmessage():
    logFormat = " %(asctime)s: %levelname(s) => %(message)s, datefmt='%y-%m-%d %I:%M:%S %p"
    log.basicConfig(filename='mylog.log',
                        filemode='w',
                        level=log.INFO,
                        format=logFormat,
                        )

    log.debug("This is Debug message")
    log.info("This is Info message")
    log.warning("This is Warning message")
    log.error("This is Error message")

    print(dir(log))


def follow(file):
    print("start following...")
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            sleep(1)
            continue
        yield line


def log_reader():
    print("start log reading...")
    with open(LogFile, 'r') as logfile:
        log_lines = follow(logfile)
        for line in log_lines:
            print(line)


def main():
    t2 = Thread(target=log_reader(), args=None)
    t1 = Thread(target=log_generator(), args=None)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    #logmessage('debug', "Log IT")


if __name__ == '__main__':
    main()
    #logmessage()