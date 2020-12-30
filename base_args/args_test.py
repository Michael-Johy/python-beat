# https://www.cnblogs.com/cwind/p/8996000.html  *args **kwargs 用法

def fun(a, b, c):
    print(a, b, c)


"""
with 3 positioned args...ok
"""
fun(1, 2, 3)

"""
array with 3 args... ok
"""
l = [1, 2, 3]
fun(*l)

"""
array with 2 args... 
"""
l1 = [1, 2]
fun(*l1, 3)  # ok
fun(*l1)  # not ok
