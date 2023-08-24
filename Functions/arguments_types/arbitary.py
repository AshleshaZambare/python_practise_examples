# 1. non keyword varibale length
def myfun(*args):
    print(args,type(args))  #<class 'tuple'>
    for i in args:
        print(i)

myfun("hello", "hi", "bye")

#2. keyword variable length
def myfun(**kwargs):
    print(kwargs, type(kwargs))
    for key, value in kwargs.items():
        print(key, value)

myfun(first = 1, two = 2, three = 3)



