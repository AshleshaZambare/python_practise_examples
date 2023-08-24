# This function modifies the global variable 's'
"""
def f():
	global s
	s += ' GFG'
	print(s)
	s = "Look for Geeksforgeeks Python Section"

	print(s)

def f1():
    s += 'gfg' #UnboundLocalError: local variable 's' referenced before assignment
    print(s)
    s = "Look for Geeksforgeeks Python Section"
    print(s)

# Global Scope
s = "Python is great!"
f1()
f()
print(s)
"""

# Python program showing a use of
# global in nested function

def add():
	x = 15
	def change():
		global x
		x = 20
	print("Before making changing: ", x)
	print("Making change")
	change()
	print("After making change: ", x)

add()
print("value of x", x)



