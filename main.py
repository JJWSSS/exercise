__author__ = 'JJW'


def modding(a, b):
    return a * b


def make_lazy(f, *args):
    return lambda: f(*args)

lazy_mod = make_lazy(modding, 4, 4)
print(lazy_mod())
