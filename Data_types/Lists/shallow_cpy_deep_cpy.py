import copy
#
# a = [1, [4, 5]]
# b = a
# a[0] = 400
# a[1][0] = 30
# a.append(8)
# a.append([6, 7])
#
# print(a)
# print(b)
# print(id(a))
# print(id(b))
# print(id(a[0]))
# print(id(b[0]))
# print(id(a[1][0]))
# print(id(b[1][0]))
#
# del b
# print("<<<<<<<<<<<<<<<<<<<<")
# print(a)
# del a
# print(a, b)


# a = [1, [4, 5]]
# shall_cp_lst = copy.copy(a)
#
# print(id(a))
# print(id(shall_cp_lst))
# print(id(a[0]))
# print(id(shall_cp_lst[0]))
# print(id(a[1]))
# print(id(shall_cp_lst[1]))
#
# a[0] = 400
# a[1][0] = 30
# a[1].append(7)
# a.append(8)
# a.append([6, 7])
#
# print(a)
# print(shall_cp_lst)
#
#

#
#
# a = [1, [4, 5]]
# deep_cp_lst = copy.deepcopy(a)
#
# print(id(a))
# print(id(deep_cp_lst))
#
# print(id(a[0]))
# print(id(deep_cp_lst[0]))

# print(id(a[1]))
# print(id(deep_cp_lst[1]))
#
# a.append(8)
# a.append([6, 7])
# a[0] = 400
# a[1][0] = 30
# a[1].append(7)
#
# print(a)
# print(deep_cp_lst)

a = 10
b = 10
list1 = [10, 10, 10]
tu = (10,)
set1 = {10}
dic = {a : 10}
print(id(a))
print(id(b))
print(id(list1[0]), id(list1[1]), id(list1[2]))
print(id(tu[0]))

print(id(dic[a]))
for i in set1:
    print(id(i))

