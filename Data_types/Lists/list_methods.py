
list1 = [1, 2, 3, 4, 5, 6]
#methods
# 1.	Append
# 2.	Insert
# 3.	Extend
# 4.	Remove
# 5.	Pop
# 6.	Clear
# 7.	Copy
# 8.	Reverse
# 9.	Sort
# 10.	count
# 11.   index

#size of list
print(len(list1))

#index
print("index =",list1.index(6))

#input the list

string = input("enter the elements:")
print(string, type(string))

lst = string.split()
print(lst, type(lst))

#Adding an element to the list
# 1. append method
lst = []
lst.append(1)
lst.append(2)
lst.append(3)
print(lst)

#2. insert method

lst.insert(3, 4)
lst.insert(9, 5)
lst.insert(0, 'geeks')
print(lst)

#3. extend method
lst1 = ['hello', 'aleins']
lst.extend(lst1)
print(lst)
lst.append(lst1)
print(lst)

#Reverse the list
list1 = [1, 2, 3, 4, 5, 6]

list1.reverse()
print(list1)

# remove the elements from the list
#1. remove-
list1.remove(3)
print(list1)

#2. Pop

list1.pop()
print(list1)
#or remove at specific index
list1.pop(0)
print(list1)

# slicing
list1 = [1, 2, 3, 4, 5, 6, 7]
print(list1[1:])
print(list1[4:2])# empty list
print(list1[2:4])
print(list1[::2])
print(list1[-1:-4: 1]) # empty list
print(list1[-1:-4: -1])

print(list1[::-1]) #reverse of list
print(list1[-6: -1])

#sort the list
list1 = [12, 3, 4, 90, 80]
list1.sort()
print(list1)
list1.sort(reverse= True)

# copy the list
list2 = list1.copy()
print("list2 = ", list2)

#count
list1 = [1, 2, 1, 3, 5, 4, 4]
print(list1.count(4))

#clear
list2.clear()
print(list2)

#list comprension
list1 = [2 * i for i in range(1, 11)]
print(list1)

#joining the two lists
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
print(list1 + list2)