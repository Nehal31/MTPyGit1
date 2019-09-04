# Functions: keyword def <fun_name> (*args, **kwargs)
# Function Argument types: No args, Positional, Name, key words


def function1():
    print("function1...")
    print("No agr function")


def function2(arg1, arg2=None):
    print("function2...")
    print("arg1 : ", arg1)
    print("arg2 : ", arg2)


def function3(*args, **kwargs):
    print("function3...")
    print("arg1 : ", args)
    print("arg2 : ", kwargs)


def main():
    function1()
    function2(10)
    function2(10, 20)
    function3(10, 20, arg=25)


if __name__ == '__main__':
    main()
