__author__ = 'JJW'
# -*- coding: utf-8 -*-


def normalize(name):
    return name[0].upper() + name[1:].lower()

print(normalize('dAAAA'))
print(list(map(normalize, ['adam', 'LISA', 'barT'])))