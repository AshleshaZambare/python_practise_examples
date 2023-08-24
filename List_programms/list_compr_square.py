square_lst = [2*i for i in range(1,11)]
print(square_lst)

sq_lst = lambda x: [x*i for i in range(1, 11)]
print(sq_lst(2))

#print even number within range
lst = [i for i in filter(lambda x: x%2 ==0, [i for i in range(1, 101)])]
sq_lst = [i for i in map(lambda x: x%2== 0, [i for i in range(1, 101)])]

print(lst)
print(">>>>>>>>>>")
print(sq_lst)

import functools

def fun(n):
    return n+n

seq = [1, 2, 3]
f = functools.reduce(lambda a, b: a+b, seq)
print(f)

cube_dict = {i : pow(i, 3) for i in range(1,11)}

print(cube_dict)

lst1 = [1, 2, 3, 4]
lst2 = ["a", "b", "c", "d"]

