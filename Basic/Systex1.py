# Syntax : Basses on Indentation
# Standard : 1 tab == 4 space

def f1():
    print("Inside f1")
    print("Indentation 1 tab = 4 space")


def f2():
  print("Inside f2")
  print("Indentation 1 tab = 2 space")


def f3():
 print("Inside f3")
 print("Indentation 1 tab = 1 space")


def f4():
        print("Inside f4")
        print("Indentation 1 tab = 8 space")


def main():
    f1()
    f2()
    f3()
    f4()

    if True:
        print('A')
        print('AA')
    if True:
            print('B')
            print('BB')
    if True:
                print('C')
                print('CC')
    """
    if True:
        print('X')
      print('XX')
    
    """


if __name__ == '__main__':
    main()