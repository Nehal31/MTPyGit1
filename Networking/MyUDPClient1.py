import socket
import time
import logging

IP = '127.0.0.1'
PORT = 5500

LOGIN_ID = '10'
PASSWARD = 'KUCHH_BHI'

def send_msg(msg):
    print("Sending msg to server:- " + msg)
    return msg.encode('utf-8')

def recv_msg(msg):
    print("Receved msg from server:- "+ msg.decode('utf-8'))
    return  msg.decode('utf-8')


def main():
    print('Creating Socket')
    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print('Server running on ' + IP + ' running at Port ' + str(PORT))
    addr = (IP, PORT)

    print('Start Conversation')
    skt.sendto(send_msg('Hi are you there ?'), addr)

    data, addr = skt.recvfrom(1024)
    recv_msg(data)
    skt.sendto(send_msg(LOGIN_ID), addr)
    data, addr = skt.recvfrom(1024)
    recv_msg(data)
    skt.sendto(send_msg(PASSWARD), addr)
    data, addr = skt.recvfrom(1024)
    recv_msg(data)
    while True:
        break

    skt.close()

if __name__ == '__main__':
    main()
