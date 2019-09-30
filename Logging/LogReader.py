from time import sleep
from threading import Thread

import logging as log
log.basicConfig(level=log.DEBUG)

LogFile = 'log.txt'

StartLog = True
PauseLog = False
StopLog = False


def follow(file):
    print("start following...")
    file.seek(0, 2)
    while StartLog:
        line = file.readline()
        if not line:
            sleep(0.1)
            continue
        yield line


def log_reader():
    print("start log reading...")
    while True:
        with open(LogFile, 'r') as logfile:
            log_lines = follow(logfile)
            for line in log_lines:
                print(line, end="")


def listener():
    log.debug('listener started...')
    print("Enter command")
    while True:
        command = input('-> ')
        if command == '':
            continue
        print(command)

    log.warning('listener stopped')
    pass


def main():
    t1 = Thread(target=listener)
    t1.start()
    t2 = Thread(target=log_reader)
    t2.start()


if __name__ == '__main__':
    main()