from threading import Thread


class MyThread(Thread):
    pass


def main():
    mt = MyThread()
    mt.setDaemon(True)


if __name__ == '__main__':
    main()