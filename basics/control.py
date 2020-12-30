from collections.abc import Iterable

nameScore = {'yt': 111, 'yp': 333}

print(nameScore['yt'])

nameScore['yt'] = 222
print(nameScore['yt'])


def trim(s):
    start = 0
    end = -1
    while s[start] == ' ':
        start = start + 1
    while s[end] == ' ':
        end = end - 1
    return s[start: end + 1]


print(trim('  aa '))


def findMinAndMax(arguments):
    _min = None
    _max = None
    if not isinstance(arguments, Iterable):
        return _min, _max

    for x in arguments:
        if _min is None or float(x) < _min:
            _min = x
        if _max is None or float(x) > _max:
            _max = x
    return _min, _max

print(findMinAndMax.__name__)

print(findMinAndMax([1, 2, 3, 4, 5, 6]))

L1 = ['adam', 'LiSA', 'barT']
L2 = list(map(str.capitalize, L1))
print(L2)

L4 = [x * x for x in range(1, 5)]
print(L4)

L5 = map(lambda x: x * x, [1, 2, 3])
print(list(L5))