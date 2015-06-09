__author__ = 'JJW'

import itertools


naturals = itertools.count(1)
ns = itertools.takewhile(lambda x: x < 10, naturals)
for i in ns:
    print(i)
for c in itertools.chain('ABC', 'DEF'):
    print(c)
for key, group in itertools.groupby('AAaBBBCCDD', lambda ch: ch.upper()):
    print(key, list(group))
