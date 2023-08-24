
# def factorial_num(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial_num(num -1)
#
# print(factorial_num(5))
# print(factorial_num(5))

#using memoization
memory = {}
def memoize_factorial(func):
    def inner_func(num):
        print("inside the inner func")
        if num not in memory:
            fact = func(num)
            memory[num] = fact
        else:
            print("returning from memory")

        return memory[num]
    return inner_func

@memoize_factorial
def factorial_num(num):
    if num == 1:
        return 1
    else:
        return num * factorial_num(num -1)

print(factorial_num(5))
print(factorial_num(5))