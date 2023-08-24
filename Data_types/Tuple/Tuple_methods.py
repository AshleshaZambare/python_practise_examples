
tuple1 = ("hello", "banana", "apple")
print(len(tuple1))

tuple1 = (1, 2, 3)
tuple2 = (2, 3, 4)

print(tuple1 + tuple2)
#we can add tuple using + operand but can not add set

#methods
#1. index
#2. count

#1. index

tuple1 = (1, 1, 2, 3, 9, 8, 9)
print("index = ", tuple1.index(9))

#2. Count
print("count", tuple1.count(9))
#create a tuple with one element
tu = ("hello")
tu1 = ("hello",)
# or
tu2 = tuple("hello")

print(type(tu)) # returns as string
print(type(tu1))
print(type(tu2))

#unpacking of tuple
fruits = ("hello", "banana", "apple", "strawberry", "berry")
var1, var2, *var3 = fruits
print(var1, var2, var3)  # hello banana ['apple', 'strawberry', 'berry']

#joining the two tuples
tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
print(tuple1+tuple2)

# multiply tuples
tuple3 = 2 * tuple1
print(tuple3)



