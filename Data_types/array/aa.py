
# a = [1, [4, 5]]
# shall_cp_lst = a
# a[0] = 400
# a[1][0] = 30
# a.append(8)
# a.append([6, 7])
#
# print(a)
# print(shall_cp_lst)
# print(id(a))
# print(id(shall_cp_lst))
# print(id(a[0]))
# print(id(a[1][0]))

import copy
a = [1, [4, 5]]
shall_cp_lst = copy.copy(a)

print(id(a))
print(id(shall_cp_lst))
print(id(a[0]))
print(id(shall_cp_lst[0]))
print(id(a[1]))
print(id(shall_cp_lst[1]))

a[0] = 400
a[1][0] = 30
a[1].append(7)
a.append(8)
a.append([6, 7])


print(a)
print(shall_cp_lst)



#
#
# a = [1, [4, 5]]
# shall_cp_lst = copy.deepcopy(a)
#
# print(id(a))
# print(id(shall_cp_lst))
# print(id(a[0]))
# print(id(shall_cp_lst[0]))
# print(id(a[1]))
# print(id(shall_cp_lst[1]))
#
# a.append(8)
# a.append([6, 7])
# a[0] = 400
# a[1][0] = 30
# a[1].append(7)

# print(a)
# print(shall_cp_lst)
