
from time import sleep
inherit_digram="""Multilevel Inheritance
                |``````````````|
                | Grand Parent |
                |,,,,,,,,,,,,,,|
                        |                   
                        |  
                |``````````````|
                |    Parent    | 
                |,,,,,,,,,,,,,,|
                        |                   
                        |  
                |``````````````|
                |      Son     | 
                |,,,,,,,,,,,,,,|
"""
class GrandParents():
    def __init__(self):
        print("Creating Grand Parent Object")

    def parent_implicit(self):
        print("Grand Parent Implicit Method")

    def override(self):
        print("Grand Parent Override Method")

    def altered(self):
        print("Grand Parent Altered Method")

class Parent(GrandParents):
    def __init__(self):
        super(Parent, self).__init__()
        print("Creating Parent Object")

    def grand_parent_implicit(self):
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
        print("Child Altered Method Befor Grand Parent altered")
        super(Parent, self).altered()
        print("Child Altered Method Befor Grand Parent ")
        super(Child, self).altered()


def main():
    son = Child()


    print("-" * 40)

    son.child_implicit()
    son.parent_implicit()
    son.grand_parent_implicit()

    print("-" * 40)

    son.override()

    print("-" * 40)

    son.altered()

    print("-" * 40)

    dad = son


if __name__ == '__main__':
    print(inherit_digram)
    sleep(2)
    main()
