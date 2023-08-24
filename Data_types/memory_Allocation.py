
a = 10
b = 10
print(a, id(a))
print(b, id(b))

a = a+1
print(a, id(a))
print(b, id(b))

a = 257
b = a
a = a+1
print(a, id(a))
print(b, id(b))

list1 = [10, 20, 30, 40]
list2 = list1
