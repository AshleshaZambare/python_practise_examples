import functools

#get the sum of list
num_lst = [1, 2, 3, 4, 5]

sum_of_lst = functools.reduce(lambda num1, num2: num1+num2, num_lst)
print("sum = ", sum_of_lst)