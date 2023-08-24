
class Person:
    """
    A class to represnt the PErson
    ...
    attributes:
    ----------
    name : str
        first name of the person
    surname : str
        last of the person
    age: int
        age of the person

    Methods:
    -------
    show(additional=""):
        prints the persons name and age.

    """
    def __init__(self, name, surname, age):
        """
        constructs all the necessary attributes for the person object

        Parameters:
            name : str
                first name of the person
            surname : str
                last of the person
            age: int
                age of the person
        """
        self.name = name
        self.surname = surname
        self.age = age

    def show(self, additional=""):
        """
        Prints the name and age of the person.
        If the argument 'additional' is passed then it gets appended after the main info.

        Parameters:
        ----------
            additional: str, optional
            more info to be displayed(default is none

        returns:
        -------
        None
        """
        print("name = ", self.name)
        print("surname = ", self.surname)
        print("age = ", self.age)
        print(f"my name is {self.name} {self.surname}, I'm {self.age} years old")
        print("my name is {} {}, I'm {} years old".format(self.name, self.surname, self.age ))
p = Person("Ashlesha", "Zambare", 28)
p.show()
print(p.__doc__)