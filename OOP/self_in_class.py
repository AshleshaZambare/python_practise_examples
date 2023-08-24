class DemoClass:
    def sample_method():
        print("This is the demo method")
the_object=DemoClass
print(dir(the_object))
# o = DemoClass().sample_method()


#
class GFG:
	def __init__(somename, name, company):
		somename.name = name
		somename.company = company

	def show(somename):
		print("Hello my name is " + somename.name +
			" and I work in "+somename.company+".")


obj = GFG("John", "GeeksForGeeks")
obj.show()

