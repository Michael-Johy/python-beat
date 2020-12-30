dic1 = {"a": "av", "b": "bv"}
print(dic1['a'])

print('a' in dic1)

dic1['a'] = 'aav'


for key in dic1:
    print("{} = {}".format(key, dic1[key]))


for key, value in dic1.items():
    print("{} = {}".format(key, value))


list1 = [1, 2, 3, 4, 5]
dic2 = {x: x * 2 for x in list1 if x % 2 == 0}
print(dic2)
