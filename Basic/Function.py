# Functions: keyword def <fun_name> (*args, **kwargs)
# Function Argument types: No args, Positional, Name, key words

def funtion1():
    print("function1...")
    print("No agr function")

def funtion2(arg1, arg2=None):
    print("function2...")
    print("arg1 : ", arg1)
    print("arg2 : ", arg2)

def function3(*args, **kwargs):
    print("function3...")
    print("arg1 : ", args)
    print("arg2 : ", kwargs)

def main():
    funtion1()
    funtion2(10)
    funtion2(10, 20)
    function3(10, 20, arg=25)

if __name__ == '__main__':
    main()
