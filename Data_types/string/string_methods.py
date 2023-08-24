

string = "geeks for geeks"
#string[0] = "H" #TypeError: 'str' object does not support item assignment
print(string)

#string with a single quote inside]
str1 = "I'm ashlesha"
#or
str2 = '''I'm ashlesha''' #it also alows multiple lines
str3 = "ff \
       dd"
print(str1)
print(str2)
print(str3)

#negative indexing
print(str1[-1])

#reverse the string
print(str1[::-1])
#or
list1 = [1, 2, 3, 4, 5]
tuple1 = (1, 3, 2, 4)
print(str(reversed(str1)))
print("".join(reversed(str1)))
print(list(reversed(list1)))
print(tuple(reversed(tuple1)))
print(str(reversed(str1)))

#update the string
str1 = "Hello I'm greek"
list1 = list(str1)
print(list1)
list1[2] = 'p'
str1 = ''.join(list1)
print(str1)

str3 = str1[0:2] + 'l' + str1[3:]
print(str3)

#deleting of a character
str1 = "hello I'm greek"
str3 = str1[0:2] + str1[3:]
print(str3)

#delete entire string
str1 = "hello hii"
list1 = [1, 2, 3]
del str1
del list1
#print(str1) #NameError: name 'str1' is not defined. Did you mean: 'str2'?
#print(list1) #NameError: name 'list1' is not defined. Did you mean: 'list'?


#Escape sequencing
str1 = '''I'm ashlesha, I'm from "Latur"'''
print(str1)

#or
str1 = "I'm from \"america\""
print(str1)

#string formatting

#default order
str1 = '{} {} {}'.format("geeks", "for", "geeks")
print(str1)

#positional formatting

str1 = '{2} {1} {0}'.format('life', "for", 'geeks')
print(str1)

#keyword formatting
str1 = '{l} {f} {g}'.format(g='greeks', f = 'for',l = 'life')
print(str1)

#format specifier
str1 = "{0:b}".format(16)
str1 = "{0:e}".format(16)
str1 = "{0:o}".format(16)
str1 = "{0:0x}".format(16)
str1 = "{0:2f}".format(16)
print(str1)

#string alignment
str1 = "|{:<10} | {:^10} | {:>10}|".format("geeks", "for", "geeks")
print(str1)
String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks",
                                                    2009)
print(String1)

#1. startswith(suffix, start, end)
string1 = "geeksforgeeks"
print(string1.startswith("geeksf"))
print(string1.startswith("geeksf", 2, 7))
#2. endswith()

string1 = "gedddgeeks"
print(string1.endswith("geeks"))


#3. isalpha()
string1 = "asbchdekd"
if string1.isalpha():
    print("string is alphabetical")

#4. isalnum()
string2 = "1234578jksd"
if string2.isalnum():
    print("string is alphanumeric")

#5. isdigit()
string3 = "12345"
if string3.isdigit():
    print("string is digits")

#6. isnumeric()
string4 = "12½"
if string4.isnumeric():
    print("string is numeric")

#7. isupper()
string7 = "AAAADD"
if string7.isupper():
    print("string is upper")

#8. islower()
string6 = "addd"
if string6.islower():
    print("string is lower")

#9. isdecimal()
string8 = "1240"
if string8.isdecimal():
    print("string is decimal")

#10. isspace()
string9 = "   "
if string9.isspace():
    print("string is containing space")

#11. isprintable()
if string8.isprintable():
    print("string is printable")

#12. isidentifier()
string10 = "ghhgh"
if string10.isidentifier():
    print("string is identifier")

string11 = "Geeks"
string12 = "geeks"
string13 = "FFFF"
#13. istitle() - a string is title cased when its first character is upper case and remaining are lower case
if string11.istitle():
    print("string is title cased")

#14. len()
print(len(string11)) #it is function

string = "jskjdkwAeife"
#15. max()
print(max(string))

#16. min()
print(min(string))

#17. upper
string = "adsgAAhd"
print(string.upper())

#18.lower()
print(string.lower())

#19. capitalize
print(string.capitalize())

#20. swapcase
print(string.swapcase())

#21.casefold
print(string.casefold())

#string alignment
#22. ljust
string = "hello"
print(string.ljust(40,"*"))


#23.rjust
print(string.rjust(40, "*"))

#24.center
print(string.center(40, "*"))

#25. zfill
print(string.zfill(20))

#remove trailing and leading white spaces
#26. strip()
string = "     hello     "
print(string.strip())


#27. lstrip()
print(string.lstrip())

#28. rstrip()
print(string.rstrip())

#29. find  - find the lowest indxex of substring matched
string = "hellohelloohellooo"
print(string.find("hello"))
print(string.find("hello", 2))

#30. rfind  - find the highest index
print(string.rfind("hello"))
print(string.rfind("hello", 2))

#31. count - no of occurances of substring
print(string.count("hello"))

#32. split - returns the list with the string after breaking given string with specified seperator
str1 = "hello, I'm ashlesha. I'am, from bhopal"
list1 = str1.split(",")
#list1 = str1.split()
print(list1)

#33 rsplit -
str1 = "hello, I'm ashlesha. I'am, from bhopal"
list1 = str1.rsplit(",")
#list1 = str1.split()
print(list1)

#34. splitlines - returns list of lines in the string
str1 = '''hellloo \n hii \n  byee byee
            i am second line
            i am third line'''
print(str1.splitlines())
