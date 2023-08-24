class Base1:
    def __init__(self):
        self.str1 = "geek1"
        print("base1")

class Base2:
    def __init__(self):
        self.str2 = "geek2"
        print("base2")

class Derived(Base1, Base2):
    def __init__(self):
        #calling constructore of base1 and base2
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printstrings(self):
        print(self.str1, self.str2)

ob = Derived()
ob.printstrings()