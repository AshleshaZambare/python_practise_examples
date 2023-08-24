import string
import random

def generate_random_password(size):
    #passwd_list = [random.choice(string.ascii_lowercase + string.ascii_lowercase + string.digits) for i in range(size)]
    #passwd = "".join(passwd_list)
    passwd = "".join([random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase) for i in range(size)])

    print(passwd)

size = 10
generate_random_password(size)