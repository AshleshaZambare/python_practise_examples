
def genator_fun():
    yield 1
    yield 2
    yield 3
x = genator_fun()
print(next(x))
print(next(x))
print(next(x))
# or
print()
for i in genator_fun():
    print(i)
print()
#program for fibonacii series
def fib_series(x):
    a, b = 0, 1
    while x :
        yield a
        c = a+b
        a = b
        b = c
        x = x-1

for i in fib_series(5):
    print(i)





