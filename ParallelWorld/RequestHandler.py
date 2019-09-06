import queue
from time import sleep
from threading import Thread
from my_logger import logger as log
#from my_command import Command as cmd


RequestQueue = queue.Queue(maxsize=0)

StopWorker1 = False
StopWorker2 = False


class Request:
    def __init__(self, command=None):
        self.command = command


def request_handler(request=None):
    log.warning("Handling Request " + request.command)
    command = request.command
    if command == 'Stop Worker 1':
        global StopWorker1
        StopWorker1 = True
    elif command == 'Stop Worker 2':
        global StopWorker2
        StopWorker2 = True
    pass


def worker1():
    log.debug('Worker 1 started...')
    while True and not StopWorker1:
        if RequestQueue.empty():
            sleep(0.1)
            continue
        log.debug('Processing request...')
        request_handler(RequestQueue.get())
    log.warning('Worker 1 stopped')


def worker2():
    log.debug('Worker 2 started...')
    while True and not StopWorker2:
        print("Enter command")
        command = input('-> ')
        new_request = Request(command=command)
        timer = 0.0
        if RequestQueue.full():
            #timer += 0.1
            sleep(timer)
            continue
        RequestQueue.put(new_request)
    log.warning('Worker 2 stopped')


def monitor():

    pass



def main():
    log.debug('Start worker thread 1')
    t1 = Thread(target=worker1)
    t1.start()

    log.debug('Start worker thread 2')
    t2 = Thread(target=worker2)
    t2.start()

    t1.join()
    t2.join()
    print("Exiting the main thread!!!")
    pass


if __name__ == '__main__':
    main()