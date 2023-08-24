# # code for testing decorator chaining
# def decor1(func):
# 	def inner():
# 		x = func()
# 		return x * x
# 	return inner
#
# def decor(func):
# 	def inner():
# 		x = func()
# 		return 2 * x
# 	return inner
#
# @decor1
# @decor
# def num():
# 	return 10
#
# @decor
# @decor1
# def num2():
# 	return 10
#
# print(num())
# print(num2())
#

def fun1(func):
    print("in decorator function1")
    def wrapper_fun():
        print("in wrapper function1")
        num = func()
        print(".............",num)
        return num * num
    print(">>>>>>>>>>>>>>>>")
    return wrapper_fun

def fun2(func):
    print("in decorator function2")
    def wrapper_fun():
        print("in wrapper function2")
        num = func()
        print(num)
        return num * 2
    print("<<<<<<<<<<<<<<<")
    return wrapper_fun

@fun1
@fun2
def get_num():
    return 10


@fun2
@fun1
def get_num1():
    return 10



print(get_num())
print(get_num1())
#it is equivalent to fun1(fun2(get_num1))