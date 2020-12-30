import numpy as np

a = np.arange(0, 100, 10)
b = a[:5]
c = a[a >= 50]

d = np.where(a < 50)
e = np.where(a >= 50)[0]

print(a)
print(b)
print(c)
print(d)
print(e)
