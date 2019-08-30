import os
import time
from threading import Thread

DIR='C:\\Users\\Nehal\\Desktop\\BigFiles'
FILE_NAME='BigFile'
FILE=DIR+'\\'+FILE_NAME
FILE_SIZE=10*1024*1024*1024 #10GB
CHUNK=2*1024*1024

def create_file(file_num):
    t = time.time()
    file = FILE + "_" + file_num
    with open(file, 'wb') as out:
        file_size = 0
        while True:
            if file_size < FILE_SIZE:
                out.write(os.urandom(CHUNK))
                file_size += CHUNK
                #print('Curr File Size', file_size)
            else:
                break
    print('Time Taken by create_file: ' + FILE_NAME + file_num + ': ', time.time() - t)

def read_file():
    t = time.time()
    with open(FILE, 'rb') as infile:
        file_size = 0
        while True:
            if file_size < FILE_SIZE:
                data = infile.read(CHUNK)
                print(len(data))
                file_size += CHUNK
                print('Read Data Size', file_size)
            else:
                break
    print('Time Taken by read_file: ', time.time() - t)

def read_file2():
    t = time.time()
    with open(FILE, 'rb') as infile:
        file_size = 0
        while True:
            if file_size < FILE_SIZE:
                data = infile.read(CHUNK)
                print(len(data))
                file_size += CHUNK
                print('Read Data Size', file_size)
            else:
                break
    print('Time Taken by read_file2 : ', time.time() - t)

def thread_main():
    print('file creation started...')
    t = time.time()
    t1 = Thread(target=create_file, args='1')
    t2 = Thread(target=create_file, args='2')
    t3 = Thread(target=create_file, args='3')

    t1.start()
    t2.start()
    t3.start()
    td = time.time() - t
    print('file creation done. Time Taken : ', td)

def main():
    print('file creation started...')
    t = time.time()
    create_file('1')
    create_file('2')
    create_file('3')
    td = time.time() - t
    print('file creation done. Time Taken : ', td)



'''
    t1 = Thread(target=create_file)
    t2 = Thread(target=read_file)
    t3 = Thread(target=read_file2)

    t1.start()
    t2.start()
    t3.start()
'''

if __name__ == '__main__':
    thread_main()

