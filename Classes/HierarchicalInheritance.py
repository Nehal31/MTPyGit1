# Single Inheritance Vs Composition
from time import sleep
inherit_digram="""Hierarchical Inheritance
                        |``````````````|
                        |   Parents    |
                        |,,,,,,,,,,,,,,|
                            |       |                        
                    .-------'       '------.
                    |                      |
               |````````````|       |````````````|
               |     SON    |       |  Daughter  |
               |,,,,,,,,,,,,|       |,,,,,,,,,,,,|
"""



class Parent:
    def __init__(self):
        print("Creating Parent Object")

    def parent_implicit(self):
        print("Parent Implicit Method")

    def override(self):
        print("Parent Override Method")

    def altered(self):
        print("Parent Altered Method")


class Son(Parent):
    def __init__(self):
        super(Son, self).__init__()
        print("Creating Child Object")

    def son_implicit(self):
        print("Son Implicit Method")

    def override(self):
        print("Son Override Method")

    def altered(self):
        print("Son Altered Method Befor Parent ")
        super(Son, self).altered()
        print("Son Altered Method After Parent ")


class Daughter(Parent):
    def __init__(self):
        super(Daughter, self).__init__()
        print("Creating Daughter Object")

    def daughter_implicit(self):
        print("Daughter Implicit Method")

    def override(self):
        print("Daughter Override Method")

    def altered(self):
        print("Daughter Altered Method Befor Parent ")
        super(Daughter, self).altered()
        print("Daughter Altered Method After Parent ")

def main():
    son = Son()
    daughter = Daughter()

    print("-" * 40)
    son.son_implicit()
    son.parent_implicit()
    daughter.daughter_implicit()
    daughter.parent_implicit()

    print("-" * 40)

    daughter.override()
    son.override()

    print("-" * 40)

    son.altered()
    daughter.altered()

    print("-" * 40)

    dad = son


if __name__ == '__main__':
    print(inherit_digram)
    sleep(2)
    main()
