
import socket
import time
import logging

IP = '127.0.0.1'
PORT = 5500

LOGIN_ID = '10'
PASSWARD = 'KUCHH_BHI'

def send_msg(msg):
    print("Sending msg to client:- " + msg)
    return msg.encode('utf-8')

def recv_msg(msg):
    print("Receved msg from client:- "+ msg.decode('utf-8'))
    return  msg.decode('utf-8')


def main():
    print('Creating Socket')
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print('Connecting to Server ' + IP + ' running at Port ' + str(PORT))
    s = skt.connect((IP, PORT))

    print('Start Conversation')
    recv_msg(skt.recv(1024))
    skt.send(send_msg(LOGIN_ID))
    recv_msg(skt.recv(1024))
    skt.send(send_msg(PASSWARD))
    recv_msg(skt.recv(1024))
    while True:
        break


    skt.close()

if __name__ == '__main__':
    main()
