# Python is a dynamically Typed language

var1 = 10
var2 = 10.0
var3 = "String"
var4 = (10, 20, "Var")
var5 = [10, 20, "Var"]
var6 = {10, 20, "Var"}
var7 = {'abc': 10,
        'xyz': 20}
var8 = lambda a: a * 2

def abc():
    print("a")
var9 = abc

import time as tm
var10 = tm

class A:
    pass
var11 = A()


print(type(var1))       # <class 'int'>
print(type(var2))       # <class 'float'>
print(type(var3))       # <class 'str'>
print(type(var4))       # <class 'tuple'>
print(type(var5))       # <class 'list'>
print(type(var6))       # <class 'set'>
print(type(var7))       # <class 'dict'>
print(type(var8))       # <class 'function'>
print(type(var9))       # <class 'function'>
print(type(var10))      # <class 'module'>
print(type(var11))      # <class '__main__.A'>


# Format :
# Use Same naming format
# e.g: class Employee:
#       emp_id, employee_id, EmpId, empId
#       name, emp_name, employee_name, EmpName, empName
#       address, emp_address, employee_address, EmpAdd, EmpAddress, empAddress
#
# 1. use underscore '_' to separate names or cammel case
# 2. It should easy to read and write



# Comment Line 1
# Comment Line 2