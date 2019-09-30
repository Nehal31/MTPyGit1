# Decorators


def wraper(func):
    def inner(a, b):
        print("File name: {}\tFunction name: {}".format(__file__, func.__name__))
        func(a, b)
    return inner


@wraper
def add(a, b):
    print("Sum of {} and {} is {}.".format(a, b, a + b))


def sub(a, b):
    print("Difference of {} and {} is {}".format(a, b, abs(a - b)))


def main():
    a = 10
    b = 20
    add(a, b)
    sub(a, b)


if __name__ == '__main__':
    main()
