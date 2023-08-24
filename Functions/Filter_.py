
#get the even number from 1 to 100
even_num_list = list(filter(lambda ele: ele%2 ==0 , [ele for ele in range(1, 101)]))
print(even_num_list)