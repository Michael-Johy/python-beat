def sign(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    else:
        return 'zero'


for x in [-1, 0, 1]:
    print(x)


# default parameter
def hello(name, upper=False):
    if upper:
        print("Hello, %s!" % name.upper())
    else:
        print("Hello, %s!" % name)


hello("aa")
hello("aa", True)
