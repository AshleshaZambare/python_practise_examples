class Person(object):
    def __init__(self, name, id):
        print("calling Person constructor")
        self.name = name
        self.id = id

    def Display(self):
        print("name = ", self.name)
        print("id = ", self.id)

class Employee(Person):


    def show(self):
        print("in Employee class")

E_obj = Employee("Ashlesha", 5210166)
print("..............")
E_obj.Display()
E_obj.show()


