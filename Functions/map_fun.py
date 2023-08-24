
#return the square of the numbers from 1 to 100

square_lst = list(map(lambda num: num*num,[num for num in range(1, 101)]))
print(square_lst)

#multiple iterator to map function using lambda

lst1 = [1, 2, 3, 4, 5]
lst2 = [2, 4, 6, 8, 10]
lst3 = [2, 4, 6, 8, 10]

sum_list = list(map(lambda n1, n2, n3: n1+n2+n3, lst1, lst2, lst3))
print(sum_list)