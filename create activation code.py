__author__ = 'JJW'


import random
import string


def create_code(length):
    chars = string.ascii_letters + string.digits
    for i in range(1, length+1):
        s = ''.join(random.sample(chars, 20))
        print(s)
create_code(10)