#check_if the string is containing digits

import string

ip_string = input("enter a string:")

for char in ip_string:
    if char not in string.digits:
        print("string is not numeric")
        break
else:
    print("string is numeric")


