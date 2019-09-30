# Operators
# Arithmetic operators: (+, -, *, /, //, %)
# Relational Operators: (>, >=, <, <=, ==, !=)
# Logical operators: (and, or, not)
# Bitwise operators: (&, |, ~, ^, >>, <<)
# Special operators: (is, is not)
# Membership operators: (in, not in)


# Arithmetic operators: (+, -, *, /, //, %)
print("Arithmetic operators: (+, -, *, /, //, %)")
# Examples of Arithmetic Operator
a = 9
b = 4

# Addition of numbers
add = a + b
# Subtraction of numbers
sub = a - b
# Multiplication of number
mul = a * b
# Division(float) of number
div1 = a / b
# Division(floor) of number
div2 = a // b
# Modulo of both number
mod = a % b

# print results
print(add)
print(sub)
print(mul)
print(div1)
print(div2)
print(mod)


# Relational Operators: (>, >=, <, <=, ==, !=)
print("Relational Operators: (>, >=, <, <=, ==, !=)")
# Examples of Relational Operators
a = 13
b = 33

# a > b is False
print(a > b)

# a < b is True
print(a < b)

# a == b is False
print(a == b)

# a != b is True
print(a != b)

# a >= b is False
print(a >= b)

# a <= b is True
print(a <= b)


# Logical operators: (and, or, not)
print("Logical operators: (and, or, not)")
# Examples of Logical Operator
a = True
b = False

# Print a and b is False
print(a and b)

# Print a or b is True
print(a or b)

# Print not a is False
print(not a)

# Bitwise operators: (&, |, ~, ^, >>, <<)
print("Bitwise operators: (&, |, ~, ^, >>, <<)")
# Examples of Bitwise operators
a = 10
b = 4

# Print bitwise AND operation
print(a & b)

# Print bitwise OR operation
print(a | b)

# Print bitwise NOT operation
print(~a)

# print bitwise XOR operation
print(a ^ b)

# print bitwise right shift operation
print(a >> 2)

# print bitwise left shift operation
print(a << 2)

# Special operators: (is, is not)
print("Special operators: (is, is not)")
# Examples of Identity operators
a1 = 3
b1 = 3
a2 = 'PythonProgram'
b2 = 'PythonProgram'
a3 = [1, 2, 3]
b3 = [1, 2, 3]

print(a1 is not b1)

print(a2 is b2)

# Output is False, since lists are mutable.
print(a3 is b3)

# Membership operators: (in, not in)
print("Membership operators: (in, not in)")
# Examples of Membership operator
x = 'Geeks for Geeks'
y = (3, 4, 5, 6)

print('G' in x)

print('geeks' not in x)

print('Geeks' not in x)

print(4 in y)

print(10 in y)
