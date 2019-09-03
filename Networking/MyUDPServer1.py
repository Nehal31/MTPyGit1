
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
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print('Bind Socket to Host ' + HOST_IP + ' at Port ' + str(PORT))
    s.bind((HOST_IP, PORT))

    print('Start Conversation')
    while True:
        data, addr = s.recvfrom(1024)
        recv_msg(data)
        s.sendto(send_msg("Login id: "), addr)
        data, addr = s.recvfrom(1024)
        id = recv_msg(data)
        s.sendto(send_msg("Password:"), addr)
        data, addr = s.recvfrom(1024)
        pwd = recv_msg(data)
        if(validate(id, pwd)):
            s.sendto(send_msg("Congrates you are a valid user"), addr)
            break
        else:
            s.sendto((send_msg("Varifaication failed, clossing the connection")), addr)
            break
    s.close()

if __name__ == '__main__':
    main()
