#! /usr/bin/python
# -*- coding: utf-8 -*-

a = 100
if a > 100:
    print(a)
elif a > 90:
    print(-a)

aa = '中文'.encode('utf-8')
print(aa)
print(len(aa))

bb = aa.decode('utf-8')
print(bb)
print(len(bb))

a = 'Hello, %s' % 'world'
print(a)


def print1(animals):
    print(animals[-1])
    print('animals length = %d' % len(animals))
    print(animals)


animals = ['dog', 'cat', 'tiger', 'fox']
print1(animals)

animals.append('git')
print1(animals)

animals.insert(1, 'pig')
print1(animals)

animals.remove('pig')
print1(animals)

if __name__ == '__main__':
    sorted()
