
import socket
import time
import logging

HOST_IP = '127.0.0.1'
PORT = 5500

CLIENT = 1

def send_msg(msg):
    print("Sending msg to client:- " + msg)
    return msg.encode('utf-8')

def recv_msg(msg):
    msg = msg.decode('utf-8')
    print("Receved msg from client:- "+ msg)
    return  msg

def validate(id,pwd):
    if id and pwd:
        return True
    else:
        return False

def main():
    print('Creating Socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print('Bind Socket to Host ' + HOST_IP + ' at Port ' + str(PORT))
    s.bind((HOST_IP, PORT))

    print('Start Listening for Client(s) ' + str(CLIENT))
    s.listen(CLIENT)

    print('Waiting for client...')
    c, addr = s.accept()

    print('Cleint details : ', c)
    print('Start Conversation')
    while True:
        c.send(send_msg("Login id: "))
        id = recv_msg(c.recv(1024))
        c.send(send_msg("Password:"))
        pwd = recv_msg(c.recv(1024))
        if( validate(id, pwd)):
            c.send(send_msg("Congrates you are a valid user"))
            break
        else:
            c.send((send_msg("Varifaication failed, clossing the connection")))
            break
    c.close()

if __name__ == '__main__':
    main()
