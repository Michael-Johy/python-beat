from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

print('p is tuple', isinstance(p, tuple))
print('p is point', isinstance(p, Point))
