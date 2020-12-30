def fun(*args):
    print(args)


def fun1(a, *args):
    print('a = ', a)
    print('args = ', args)


def fun2(a=None, *args):
    print('a = ', a)
    print('args = ', args)


fun(1)  # ok

fun(11, 1, 111)  # ok

fun1(1, [11, 12, 13])

fun2(1)
