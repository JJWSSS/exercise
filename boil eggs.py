__author__ = 'JJW'


def cooking_time(eggs):
    if 0 != eggs % 8:
        return (eggs//8+1)*5
    else:
        return (eggs//8)*5

print(cooking_time(10))