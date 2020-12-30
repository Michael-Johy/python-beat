import numpy as np

# 2d array
my_array2d_01 = np.zeros((2, 3), int)
print(my_array2d_01)

my_array2d_02 = np.random.random((2, 4))
print(my_array2d_02)
print(my_array2d_02[1, 2])

# column
print(my_array2d_02[:, 1])

array01 = np.array([[1, 2], [3, 4]])
array02 = np.array([[11, 12], [13, 14]])

sum1 = array01 + array02
reduce1 = array01 - array02
product1 = array01 * array02
quotient = array01 / array02

print(" Sum = {}".format(sum1))
print(" Reduce = {}".format(reduce1))
print(" Product = {}".format(product1))
print(" Quotient = {}".format(quotient))
