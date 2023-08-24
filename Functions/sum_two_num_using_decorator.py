def hello_decorator(func):
    print("in decorator function")
    def wrapper_fun_for_sum(*args):
        print("in wrapper function")
        sum = func(*args)
        print("exiting from wrapper function")
        return sum
    print(id(wrapper_fun_for_sum))
    return wrapper_fun_for_sum

@hello_decorator
def sum_two_number(a, b):
    print("in sum fun")
    return a+b

# print(id(sum_two_number))
# sum_two_number = hello_decorator(sum_two_number)
# print(id(sum_two_number))
# print("sum = ",sum_two_number(2, 3))
#

print("sum = ",sum_two_number(2, 3))
