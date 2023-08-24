#1. function are objects
def shout(text):
    return text.upper()

print(shout("hello"))
yell = shout
print(yell("hello"))

#2. function cane be passed as an argument to the another function
def whisper(text):
    return text.lower()

def greet(func):
    text = func("i am created by a func which is passed as an argument")
    print(text)

greet(whisper)
greet(shout)

#function can return from another function
def create_adder(x):
    def adder(y):
        return  x+y

    return adder

add_15 = create_adder(15)
addition = add_15(10)
print(addition)
