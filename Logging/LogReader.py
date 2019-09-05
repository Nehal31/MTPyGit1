from time import sleep
from threading import Thread

LogFile = 'log.txt'

def follow(file):
    print("start following...")
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            sleep(0.1)
            continue
        yield line


def log_reader():
    print("start log reading...")
    with open(LogFile, 'r') as logfile:
        log_lines = follow(logfile)
        for line in log_lines:
            print(line, end="")


def listener():


def main():
    t1 = Thread(target=listener(), args=None )

    t2 = Thread(target=log_reader(), args=None)
    t2.start()
    t2.join()


if __name__ == '__main__':
    main()