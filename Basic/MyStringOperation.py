str1 = "This is a String line belongs to the str1"
str2 = "This is a String Paragraph belongs to the str2 \nLine 1\nLine 2\nLine End."
str3 = """This is a Multiline String Paragraph belongs to the str3
Line 1
Line 2
Line End."""

print(str1)
print(str2)
print(str3)

"""
Output
This is a String line belongs to the str1
This is a String Paragraph belongs to the str2 
Line 1
Line 2
Line End.
This is a Multiline String Paragraph belongs to the str3
Line 1
Line 2
Line End. 
"""
print("%r" % str1)
print("%r" % str2)
print("%r" % str3)

"""
Row Output:
'This is a String line belongs to the str1'
'This is a String Paragraph belongs to the str2 \nLine 1\nLine 2\nLine End.'
'This is a Multiline String Paragraph belongs to the str3\nLine 1\nLine 2\nLine End.'
"""

str4 = 'This is a String line belongs'
str5 = 'This is a String line belongs to the str1'
str6 = str1
print('str1',id(str1))      # str1 2765852305616
print('str4', id(str4))     # str4 2765849472176
print('str5', id(str5))     # str5 2765852305616
print('str6', id(str6))     # str6 2765852305616
print('-' * 40)
# ----------------------------------------------------------------------------------

str7 = "   This is  String having lots of Extra spaces.    "
print("%r" % str7)  # '   This is  String having lots of Extra spaces.    '
str8 = str7.strip()
print("%r" % str8 )  # 'This is  String having lots of Extra spaces.'
print('-' * 40)
# -----------------------------------------------------------------------------------

str9 = str1.encode(encoding='utf-8', errors='stricts')
print("%r" % str9 )     # b'This is a String line belongs to the str1'
print('-' * 40)
# -----------------------------------------------------------------------------------
print("%r" % 'apple is apple'.capitalize() )    # 'Apple is apple'
print("%r" % 'Apple is apple'.capitalize() )    # 'Apple is apple'
print('-' * 40)
# ------------------------------------------------------------------------------------

print("%r" % "APPLE IS APPLE".casefold() )    # 'apple is apple'
print("%r" % 'apple is apple'.casefold() )    # 'apple is apple'
print("%r" % 'Apple is apple'.casefold() )    # 'apple is apple'
print('-' * 40)
# ------------------------------------------------------------------------------------

print("%r" % 'apple is apple'.upper() )    # 'APPLE IS APPLE'
print("%r" % 'Apple is apple'.upper() )    # 'APPLE IS APPLE'
print('-' * 40)
# ------------------------------------------------------------------------------------

print("%r" % 'APPLE IS APPLE'.lower() )    # 'apple is apple'
print('-' * 40)
# ------------------------------------------------------------------------------------

print("%r" % 'apple is apple'.endswith('app'))     # False
print("%r" % 'apple is apple'.endswith('apple'))   # True
print('-' * 40)
# ------------------------------------------------------------------------------------

print("%r" % 'apple is apple'.count('a'))      # 2
print("%r" % 'apple is apple'.count('p'))      # 4
print("%r" % 'apple is apple'.count('x'))      # 0
print('-' * 40)
# -------------------------------------------------------------------------------------

print("%r" % 'apple is apple'.center(20))       # '   apple is apple   '
print("%r" % 'apple is apple'.center(20,'X'))   # 'XXXapple is appleXXX'
print('-' * 40)
# -------------------------------------------------------------------------------------

print("%r" % len('apple is apple'))     # 14
print('-' * 40)
# -------------------------------------------------------------------------------------

print("%r" % 'apple \t is \t apple'.expandtabs(tabsize=10))     # 'apple      is        apple'
print('-' * 40)
# -------------------------------------------------------------------------------------

print("%r" % 'apple \t is \t apple'.find('\t'))     # 6
print("%r" % 'apple is apple'.find('a'))            # 0
print('-' * 40)
# -------------------------------------------------------------------------------------

print("%r" % 'apple is apple'.isascii())
print("%r" % ''.isascii())

# --------------------------------------------------------------------------------------

for index, i in enumerate(range(2250, 2500)):
    print(i , chr(i))

fname = [2344, 2375, 2361, 2366, 2354, 32 ]
mname = [2325, 2369, 2350, 2366, 2352]
name = fname + mname
for char in name:
    print(chr(char), end='')

# ---------------------------------------------------------------------------------------
