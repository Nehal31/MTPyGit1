# Parsing arguments
# Unpacking them
# File operation: read, readline, readlines, close, write, truncate

from sys import argv


def file_operation():
    script, file1, file2 = argv
    fd = open(file1, 'rt')
    data = fd.readline()
    print("%r"%(data))
    fd.close()


def main():
    script, first, second = argv
    print("Script name : ", script )
    print("First argv : ", first )
    print("Second argv : ", second )

    print("argvs : ", argv, type(argv) )

    print("Need More Arguments : ")
    third = input('->')
    print("Third argv : ", third )


if __name__ == '__main__':
    file_operation()

