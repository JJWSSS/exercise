__author__ = 'JJW'


def unlimited_sum(*args):
    usum = 0
    for num in args:
        usum += num
    return usum
print(unlimited_sum(1, 2, 4))