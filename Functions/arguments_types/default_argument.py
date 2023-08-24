
# def fun(var):
#     print("in function")
#     print("var=", var)
#
#
# fun() # TypeError: fun() missing 1 required positional argument: 'var' if the default parameter is not used

def fun(var=10):
    print("in function")
    print("var=", var)

fun()