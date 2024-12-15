class one:
    def __init__(self, num):
        self.num = num
    def __add__(self, b):
        return self.num*b.num
a = one(5)
b = one(6)
print(a+b)