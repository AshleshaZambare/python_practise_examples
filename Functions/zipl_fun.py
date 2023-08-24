lst1 = [1, 2, 3, 4, 5]
tuple1 = ('a', 'b', 'c', 'd', 'e')

result = zip(lst1, tuple1)
print(result, type(result))
print(list(result))

print(list(zip()))
print(list(zip(lst1)))

t = (3)
print(t, type(t))
t = (3,)
print(t, type(t))
