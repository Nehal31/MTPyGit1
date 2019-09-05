import pickle

class Employee:
    def __init__(self, eid, name, salary = None):
        self.eid = eid
        self.name = name
        self.salary = salary

    def salaryRaise(self, increment):
        self.salary *= increment
        print(self.salary)

def main():
    name = 'Nehal Ram'
    eid  = 'ABC'
    sal = 100
    emp = Employee(name, eid, sal)

    emp.salaryRaise(1.25)
    with open('pickle_dump_emp1', 'wb') as pd:
        print(emp)
        emp_pickle_dump = pickle.dumps(emp)
        print("%r"%emp_pickle_dump)
        pd.write(emp_pickle_dump)

    with open('pickle_dump_emp1', 'rb') as pd:
        emp_data = pd.read()
        print("%r"%emp_data)
        emp = pickle.loads(emp_data)
        print(emp)


if __name__ == '__main__':
    main()
