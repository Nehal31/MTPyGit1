# lambda function

# def add(x, y):
#   return x + y      
add = lambda x, y: x + y
sub = lambda x, y: x - y

my_op = lambda x: x + x + x + x


def main():
    a = 10
    b = 20
    print(add(a, b))
    print(sub(a, b))
    print(my_op(a))


if __name__ == '__main__':
    main()
