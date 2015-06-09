__author__ = 'JJW'

from collections import namedtuple, deque, defaultdict


Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
q = deque(['a', 'b', 'c'])
print(q.append(10))
print(q.appendleft(1))
print(q.pop())
print(q.popleft())
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['abc'])

