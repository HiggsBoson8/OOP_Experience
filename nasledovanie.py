class A:
    def __init__(self):
        self.a = 5
        self.b = 10

class B:
    def __init__(self, b):
        self.b = b

class C:
    def __init__(self, c):
        self.c = c


a = A()
b = B(a)
c = C(b)

print(c.c.b.a)

print()



