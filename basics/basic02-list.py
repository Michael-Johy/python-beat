# container
list1 = ["1", "2", "3"]
print('{} length =  {}'.format(list1, len(list1)))
list1[2] = "foo"
print('{} length =  {}'.format(list1, len(list1)))
list1.append("4")
print('{} length =  {}'.format(list1, len(list1)))
list1.remove("1")
print('{} length =  {}'.format(list1, len(list1)))

# range
listRange = list(range(1, 10, 2))
print(listRange)
print(listRange[2:3]);

# for
for x in listRange:
    print(x)

for index, item in enumerate(listRange):
    print("%d  =  %s " % (index, item))

list2 = [x * 2 for x in listRange]
print(list2)
