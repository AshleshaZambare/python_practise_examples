class Person:
    def __init__(self):
        print("constructor is called")

    def __del__(self):
        print("destructor is called")

p = Person()
