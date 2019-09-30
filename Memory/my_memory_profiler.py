

@profile
def my_func():
    a = ([1].append(1) for _ in (range(10 ** 6)))
    b = ([2].append(2) for _ in (range(2 * 10 ** 7)))
    c = range(2 * 10 ** 7)
    d = [i for i in range(2 ** 10)]
    print(type(d))
    del b
    return a


if __name__ == '__main__':
    my_func()
