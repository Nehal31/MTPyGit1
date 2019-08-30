import socket
from time import time,sleep
from threading import Thread


SERVER = 'www.google.com'
PORT = 80
TIMEOUT = 2


def is_connected():
    try:
        address = socket.gethostbyname(SERVER)
        s = socket.create_connection(address=(address, PORT), timeout=TIMEOUT)
        s.close()
        return True
    except Exception as e:
        print(e)
        pass

    return False


def check_connection():
    while True:
        if is_connected():
            print("Internet Available!!!")
        else:
            print("No Internet!!!")
            break
        sleep(2)


def main():

    t1 = Thread(target=check_connection)
    t1.start()

    t1.join()


if __name__ == '__main__':
    main()