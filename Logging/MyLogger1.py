import time
import logging as log
import os

'''
Log Levels :
    NOTSET = 0
    DEBUG = 10
    INFO = 20
    WARNING = 30  ** Default
    ERROR = 40
    CRITICAL = 50
    
File Name :
    Default = stderr
    
Format :
    Default < Log Level >:< root >:< message > 
    "%(asctime)s **%(levelname)s** %(message)s"
'''


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def main():
    pass


start = time.time()
log.basicConfig(filename='log.txt',
                level=log.DEBUG,
                format="%(asctime)s **%(levelname)s** %(message)s")
a = 10
b = 5
log.debug("Add Operations : {} + {} = {}".format(a, b, add(a, b)))
log.info("Sub Operations : {} + {} = {}".format(a, b, sub(a, b)))
log.warning("Mul Operations : {} + {} = {}".format(a, b, mul(a, b)))
log.error("Div Operations : {} + {} = {}".format(a, b, div(a, b)))
end = time.time()
log.debug("Execution time : {}".format(end - start) )