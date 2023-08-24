class Base(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Child(Base):
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

    def get_age(self):
        return self.age

class Grandchild(Child):
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    def get_address(self):
        return self.address

ob = Grandchild("Ashlesha", 27, "Pune")
print(ob.get_name())
print(ob.get_age())
print(ob.get_address())