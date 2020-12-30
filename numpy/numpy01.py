import numpy as np

# 1d array
list1 = [1, 2, 3, 4, 5]
print(list1)
my_array = np.array(list1)
print(my_array)
print(my_array.shape)

idx = 0
print("{} - {} = {}".format(my_array, idx, my_array[idx]))

my_array[0] = 9
print(my_array[0])

my_array01 = np.zeros(5, int)
print(my_array01)

my_array02 = np.random.random(5)
print(my_array02)

