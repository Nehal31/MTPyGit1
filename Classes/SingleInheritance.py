# Single Inheritance Vs Composition
from time import sleep
inherit_digram="""Single Inheritance
                |``````````````|
                |    Parent    | 
                |,,,,,,,,,,,,,,|
                        |                   
                        |  
                |``````````````|
                |      Son     | 
                |,,,,,,,,,,,,,,|
"""

class Parent():
    def __init__(self):
        print("Creating Parent Object")

    def parent_implicit(self):
        print("Parent Implicit Method")

    def override(self):
        print("Parent Override Method")

    def altered(self):
        print("Parent Altered Method")


class Child(Parent):
    def __init__(self):
        super(Child, self).__init__()
        print("Creating Child Object")

    def child_implicit(self):
        print("Child Implicit Method")

    def override(self):
        print("Child Override Method")

    def altered(self):
        print("Child Altered Method Befor Parent ")
        super(Child, self).altered()
        print("Child Altered Method After Parent ")


def main():
    dad = Parent()
    son = Child()

    print("-" * 40)

    dad.parent_implicit()
    son.child_implicit()
    son.parent_implicit()

    print("-" * 40)

    dad.override()
    son.override()

    print("-" * 40)

    dad.altered()
    son.altered()

    print("-" * 40)

    dad = son


if __name__ == '__main__':
    print(inherit_digram)
    sleep(2)
    main()
