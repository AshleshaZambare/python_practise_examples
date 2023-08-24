
def fun():
    yield 1
    yield 2
    yield 3

for value in fun():
    print(value)

print()
def nextsquare():

    def fun():
        for i in range(1, 11):
            yield i*i

    for square_val in fun():
        print(square_val)

nextsquare()
