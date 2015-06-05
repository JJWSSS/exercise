__author__ = 'JJW'
# -*- coding: utf-8 -*-


def triangles():
    l1 = [1]
    l2 = []
    while True:
        for i in range(len(l1)-1):
            l2.append(l1[i]+l1[i+1])
        l2.append(1)
        yield l2
        l1 = l2
        l2 = [1]

tr = triangles()
num = 0
for n in tr:
    print(n)
    if num == 9:
        break
    num += 1
