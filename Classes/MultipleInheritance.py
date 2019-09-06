# Single Inheritance Vs Composition
from time import sleep
inherit_digram="""Multiple Inheritance
               |````````````|        |````````````|
               |     Mom    |        |     Dad    |
               |,,,,,,,,,,,,|        |,,,,,,,,,,,,|
                    |                      |   
                    '-------.      .-------' 
                            |      |           
                        |``````````````|
                        |   Child      |
                        |,,,,,,,,,,,,,,|
"""

class Dad:
    def __init__(self):
        print("Creating Dad Object")

    def dad_implicit(self):
        print("Dad Implicit Method")

    def override(self):
        print("Dad Override Method")

    def altered(self):
        print("Dad Altered Method")

    def parent(self):
        print("Dad Parent Method")


class Mom:
    def __init__(self):
        print("Creating Mom Object")

    def mom_implicit(self):
        print("Mom Implicit Method")

    def override(self):
        print("Mom Override Method")

    def altered(self):
        print("Mom Altered Method")

    def parent(self):
        print("Mom Parent Method")


class Child(Dad, Mom): # Inheritance Priority FIFS Dad is having more priority compare to mom
    def __init__(self):
        super(Child, self).__init__()
        print("Creating Child Object")

    def child_implicit(self):
        print("Child Implicit Method")

    def override(self):
        print("Child Override Method")

    def altered(self):
        print("Child Altered Method Befor Dad/Mom ")
        super(Child, self).altered()
        print("Child Altered Method Befor Dad/Mom ")

def main():
    son = Child()


    print("-" * 40)

    son.child_implicit()
    son.dad_implicit()
    son.mom_implicit()

    print("-" * 40)

    son.override()

    print("-" * 40)

    son.parent()

    print("-" * 40)

    son.altered()

    print("-" * 40)

    dad = son


if __name__ == '__main__':
    print(inherit_digram)
    sleep(2)
    main()
