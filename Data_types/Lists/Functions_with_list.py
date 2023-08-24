# Sum
# len
# max
# min
# all
# any
# ord
#sorted

# enumerate
# filter
# map
# lambda
# accumlate
# reduce

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5, 6, 7]

list3 = (True, True, False)
list4 = (True, True, True)
list5 = [80, 90, 70, 10]

print(sorted(list5))
print(sum(list1))
print(len(list1))
print(max(list1))
print(min(list1))

print(all(list1))
print(all(list3))
print(all(list4))

print(any(list3))
print(any(list1))
print(any(list4))

print(ord("A"))  #returns the unicode character for the string - it is opposite of chr() function
print(chr(67))

print(enumerate(list1))
for ele in enumerate(list1):
    print(ele)

def func(ele):
    vow_list = ["a", "e", "i", "o", "u"]
    if ele not in vow_list:
        return False
    else:
        return True
list1 = ["a", "e", "f", "g", "h"]
filter_obj = filter(func, list1)
print(list(filter_obj))

for ele in filter_obj:
    print(ele)


#map

list1 = [1, 2, 3, 4]
def func1(n):
    return n+n
map_obj = map(func1, list1)

print(list(map_obj))

#lambda


is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]

# iterate on each lambda function
# and invoke the function to get the calculated value
for item in is_even_list:
    print(item())
