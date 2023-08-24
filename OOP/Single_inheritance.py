class Person(object):
    def __init__(self, name, id):
        print("calling Person constructor")
        self.name = name
        self.id = id

    def Display(self):
        print("name = ", self.name)
        print("id = ", self.id)

class Employee(Person):
    def __init__(self, name, id, salary, post):
        print("calling Employee constructor")
        self.salary = salary
        self.post = post

        Person.__init__(self, name, id)
        #super().__init__(name, id)
    def show(self):
        print("in Employee class")
        print("salary = ", self.salary)
        print("post = ", self.post)

E_obj = Employee("Ashlesha", 5210166, 12000000, 'Software Engineer')
print("..............")
E_obj.Display()
E_obj.show()







