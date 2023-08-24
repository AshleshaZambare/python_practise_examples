
set1 = {1, 2, 3, 4}
print(set1)

set1 = {1, 2, 3}
set2 = {2, 3, 4}
#print(set1 + set2) #TypeError: unsupported operand type(s) for +: 'set' and 'set'

# creating blank set
set2 = set()
print(set2)
set1 = {}
print(type(set1))

# set2()
#set using string
string = "geeksforgeeks"
print(set(string)) #{'s', 'o', 'g', 'r', 'k', 'e', 'f'}

#set using list
list1 = ['geeks', 'for', 'geeks']
print(set(list1))  #{'for', 'geeks'}

# Methods

# 1. add
set1 = {1, 2, 3, 3 ,4}
set1.add(9)
set1.add((6,7))
# dictionary and list can not be added to set as they are not hashable whereas tuple can be added as it is hashable
#set1.add([2, 3]) #TypeError: unhashable type: 'list'
#set1.add({'h':2}) #TypeError: unhashable type: 'dict'
print(set1)

# 2. update - for adding two or elements -- can use list, dictionary, tuple, string
set1.update([15, 20])
set1.update({'bricks': '3'})
set1.update("vijay")
print(set1)

#3. remove
set1 = {1, 2, 3, 4, 5}
set1.remove(5)
print(set1)

#4. discard
set1.discard(3)
print(set1)

#pop
set1.pop()
print(set1)

#clear
set1.clear()
print(set1)

#frozenset
set1 = {1, 2, 3, 4, 5, 5}
set1.add(9)
print(set1)
fset1= frozenset(set1)
#fset1.add(4) #AttributeError: 'frozenset' object has no attribute 'add'

#union - ekatra krte
set1 = {2, 4, 6, 8, 10}
set2 = {3, 6, 9, 12, 10}
list2 = [2, 4, 5, 6]
print("union = ",set1.union(set2))
print("union =", set1.union(list2))

#intersection - doghatle common
print(set1.intersection(set2)) #

#difference - pahilyatle vegle common sodun
print(set1.difference(set2))

#symmetric difference  - common sodun doghatle vegle
print(set1.symmetric_difference(set2))

#issubet
set1 = {1, 2}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))

#issuperset
print(set2.issuperset(set1))

#isdisjoint - vegle astil tr true
set1 = {1, 2, 3}
set2 = {2, 4}
set3 = {5, 6, 7}
print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))


##empty frozen set
fset = frozenset()


