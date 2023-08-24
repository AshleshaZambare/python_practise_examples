
def fun(x, y, z):
    print("in function")
    print(x, y, z)


fun(x= 1,z = "hello", y = "hi")
fun( "hi", y = 1,z = "hello")
#fun( x= "hi", y = 1, "hello") # SyntaxError: positional argument follows keyword argument

