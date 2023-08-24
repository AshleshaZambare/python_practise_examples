import array

import array as arr
#array

#creating an array
#elements are of integer type
ar = array.array('i', [1, 2, 3])
print(ar)

#for i in arr:
    #print(i, type(i)) #TypeError: 'module' object is not iterable

for i in range(0, len(ar)):
    print(ar[i], type(ar[i]))

#creating array with double type
ar = array.array('d', [1.2, 2.3, 3.4])
print(ar)

for i in range(0, len(ar)):
    print(ar[i], type(ar[i]))

#1. add an element to an array
ar = array.array('i', [1, 2, 3])
ar.insert(1,4)
print(ar)

#2. or using append at the last
ar.append(6)
print(ar)

#removing an elements from array
#3. remove
ar.remove(6)
print(ar)

#4. pop
ar.pop()
print(ar)
ar.pop(1)
print(ar)

#5.extend
ar.extend([2, 2, 2])
print(ar)

