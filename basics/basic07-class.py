class Greeter(object):
    def __init__(self, name):
        self.name = name

    def greet(self, upper=False):
        if upper:
            print("Hello, %s !" % self.name.upper())
        else:
            print("Hello, %s !" % self.name)


g = Greeter("Fred")
g.greet()
g.greet(True)
