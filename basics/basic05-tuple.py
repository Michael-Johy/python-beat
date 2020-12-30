tuple1 = (1, 2, 3, 4)
for item in tuple1:
    print(item)

dic1 = {(x, x + 1): x for x in tuple1}
print(dic1)

print(dic1[(1, 2)])
