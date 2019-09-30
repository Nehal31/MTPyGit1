# String Operation


str1 = "String"
str2 = 'String'
str3 = """String"""

print(str1)
print(str2)
print(str3)


char = 'A'
integer = ord(char)     # ascii value
print(integer)
char = chr(integer)
print(char)


"""
define        :  city="Bengaluru"
lenght        :  len(city)
first char    :  city[0]
last char     :  city[-1]
reverse       :  city[::-1]
first 4 chars :  city[0:4]
last  4 chars :  city[-4:]
others        :  city[2:-2] excluding first 2 & last 2 chars 
              :  city[-5:-2]               
Add 2 strs    :  "hello " + city
Cmp 2 strs    :  if city == "pune":
search - str  :  if "uru" in city
uppercase     :  city.upper()
swap          :  city.swapcase()
count repeat  :  city.count("u")
Index         :  city.index("a") 
Rindex        :  city.rindex("a")
trim          :  city.strip()
replace       :  city.replace("i","p")
starts with   :  city.startswith("ben")
chk for int   :  city.isdigits()
"""



"""
Q. Write a program to accept a string from the user and convert the first letter & last letter to upper case
sample input : new way
     output  : New waY

text=input("enter the data : ")
text=text[0].upper()+text[1:-1]+text[-1].upper()
print(text)

Q. Write a program to accept a string from the user and convert the first 4 chars to UPPERCASE
u have to reverse the last 4 chars & conver to UPPERCASE

sample input:  hello world of perl
      output:  HELLo world of lrep

text=input("enter the data : ")

text=text[0:4].upper()+text[4:-4]+text[:-5:-1].upper()
text=text[0:4].upper()+text[4:-4]+text[-4:].upper()[::-1]
print(text)



ex:
num = input("Enter a number : ")
if num.isdigit():
  num = int(num)
  num+=5
  print(num)
else:
  print("Invalid input")

print("Hello")

----------------------------------------------------------
"""


name = "hari parsad udupa"
words = name.split()
print(words)

res = "".join(words)
print(res)



