# List
# Tuple
# Set
# Dictionary
# Frozen Set

"""
Define       :  arr = [10,20,30,40,50]
                arr = [] or list()    # Empty List
                arr = list(range(10, 51, 10))
Length       :  len(arr)
First elem   :  arr[0]
Add a elem   :  arr.append(element)
                arr.insert(position, element)
                arr.extend(list of elements)
Delete  elem :  del arr[0]
                arr.pop(position)
                arr.pop()   Default is -1
                arr.remove(element)
search       :  element in list
Compare lists:  list1 == list2
Add 2 list   :  res = list1 + list2
Sort         :  arr.sort()
Reverse      :  arr.reverse()
Count        :  arr.count(10)
Index        :  arr.index(5)
Rindex       :  arr.rindex(5)
sum/max/min  :  sum(arr)
"""

# =================================================================

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9]
print("Original list:", l)

print("Add element:100, by default last index")
l.append(100)
print(l)

print("Add element in specified index, index 5, value 110")
l.insert(5, 110)
print(l)

print("Add all elements of list l2 to the existing list l")
l2 = [10, 15, 20, 35]
l.extend(l2)
print(l2)

print("remove element by index")
a = l.pop()     # remove and return last element
print(a, l)
l.pop(5)
print(l)
del l[0]
print(l)

print("Remove element by value")
l.remove(9)
print(l)

print("Count of value 9 is : ", l.count(9))
print("Value is in index 5 : ", l.index(5))


l.reverse()
print("Reverse of list :", l)
l.sort()
print("Sorting of list :", l)


max_val = max(l)
min_val = min(l)
sum_val = sum(l)
print("max_val : ", max_val)
print("min_val : ", min_val)
print("sum : ", sum_val)


print("Remove all the elements from the list :", l)
l.clear()
print(l)


'''
list.sort(key=None,reverse=False)

key = a function which accepts one args & Return a value

reverse = True    - desc order
reverse = False   - asc order

'''

studs = ['manu-43', 'john-54', 'hari-45', 'arun-67', 'somu-76']
studs.sort(key=lambda x:int(x.split("-")[1]), reverse=True)
print("\n".join(studs))


"""
Note:
    temp=arr[:]
    temp.sort()     # In-Place Sort
    OR
    temp=sorted(arr)  # call by value sort


    temp=arr[:]
    temp.revrese()
    OR
    temp=reversed(arr)

----------------------------------------------------------
@. Create a list with a name as "values" with 10 elements every element initialized to ZERO
Ans: values = [0]*10

@. Create a list with a name as "values" with 10 elements every element initialized 1 to 10
Ans:  values = list(range(1,11))

----------------------------------------------------------
"""

"""
Define       :  tup = (10,20,30,40,50)
                tup = tuple()    # Empty List
                tup = tuple(range(10, 51, 10))
Length       :  len(tup)
First elem   :  tup[0]
Add a elem   :  Not Possible
Delete  elem :  Not Possible
search       :  elm in tup
Compare lists:  list1 == list2
Add 2 list   :  res = list1 + list2
Sort         :  tup2 = sorted(tup)
Reverse      :  tup = reverse(tup)
Count        :  tup.count(10)
Index        :  tup.index(5)
Rindex       :  tup.rindex(5)
sum/max/min  :  sum(arr)
"""
print("Create tuples")
tup = tuple()
print(type(tup), tup)            # <class 'tuple'>
tup2 = (10,)
print(type(tup2), tup2)           # <class 'tuple'>

not_a_tup = (10)
print(type(not_a_tup))      # <class 'int'>

tup3 = tuple(range(1, 10))
print(type(tup3), tup3)

print("Length of tuple : ", len(tup3))



"""
Dict:-
======

declare       : studs={"arun":10,"ajit":20,"hari":30}
length        : len(studs)
val of arun   : studs['arun']
Incr val ajit : studs['ajit'] = studs['ajit'] + 5
Add new elem  : studs['john'] = 40   ******VERY IMP*****
delete        : del studs['hari']
search        : if("mani" in studs):
keys          : res = studs.keys()
vals          : res = studs.values()

for key in studs:
  print key,studs[key]

	d = {'name':'tom','age':'7','Class':'3'}
	# To get single element
	print(d['name'])
	#print(d['mobile'])
	#print(d.get('mobile','Not found'))
	print("All : ",d.items())
	print("Keys :",d.keys())
	print("Values : ",d.values())

	# To add new element
	d['mobile'] = '12345'
	d.update({'mob':45678})

	# To remove element
	d.pop('mob')
	print(d)

==========================================================
sort the dictionary:-
=====================

zones={'south':56,'west':23,'east':45,'north':37}

#based on key
for key in sorted(zones):
  print(key,zones[key])

print()

#based on value
for key in sorted(zones,key=lambda x:zones[x]):
  print(key,zones[key])


==========================================================

Note: other derived classes
>>array       - same type
>>collections - dequeue, orddict,counter,namedtuple
>>bisect      - algo
>>heapq       - algo


set:-
=====
 >> un ordered data structure
 >> elminate the duplicates
 >> union
    difference
    insersection
    issubset
    issuperset

ex:-
----
a = [10,20,30,40,50,60,70,10]

b = [10,40,70,90,15,32,54]


#what is common b/w a & b ?

res = set(a) & set(b)

print(res)

#what is unique in first list ?

print(set(a)-set(b))
"""