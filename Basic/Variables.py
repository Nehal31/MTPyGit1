# Variables can be anything starts with '[a-zA-Z_][a-zA-Z0-9_]*'
# Variable Should be some meaningful name

cars = 4
car_drivers = 4
no_of_passengers = 16
distance = 10.5
distance_unit = 'k.m'
distance_traveled = 5.5

# Bad variables declaration
# SyntaxError: invalid syntax
# 3name = 'Number Name'


# Printing
print(f"Total no of cars {cars}")
print(f"Total no. of drives {car_drivers}")
print(f"Total no of passengers {no_of_passengers}")
print(f"Total distance from city A to B : {distance}")
print(f"Total distance traveled : {distance_traveled} ")
print(f"Each car is having '{ distance / cars }' no of traveler ")
print(f"Total distance need to be travel : {distance - distance_traveled} ")

# undef variable : uncomment to see errors
# NameError: name 'not_defined' is not defined
# print(f"undefined variable {not_defined} ")

# SyntaxError: f-string: empty expression not allowed
# print(f"Total distance traveled : {} ")

print('=' * 60)
# Printing using format method
print("Total no of cars : {}".format(cars))
print("Total no. of drives : {}".format(car_drivers))
print("Total no of passengers : {}".format(no_of_passengers))
print("Total distance from city A to B : {}".format(distance))
print("Total distance traveled : {}".format(distance_traveled))
print("Each car is having '{}' no of traveler ".format(distance / cars))
print("Total distance need to be travel : {} ".format(distance - distance_traveled))


print('=' * 60)
print("ESCAPE Sequences...")
print("Bell : \a")
print("Backslash : aaa\\aaa")
print("Single Quote : aaa\'aaa")
print("Double Quote : aaa\"aaa")
print("Back Space : aaa\baaa")
print("Form feed : aaa\faaa")
print("Line feed : aaa\naaa")
#print("Unicode character : aaa\N{a}")
print("Carriage return : aaa\raaa")
print("Horizontal tab : aaa\taaa")
#print("16 bit hex character : aaa\uaaa")
#print("32 bit hex character : aaa\Uaaa")
print("Octal Value : aaa\oooaaa")
print("Hex Value : aaa\xaa")





print('=' * 60)


