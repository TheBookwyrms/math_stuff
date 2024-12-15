class testing:
    def __init__(self, value):
        self.x = value
    
    def __add__(self, b):
        return self.x + b.x + b.x
    
t1 = testing(5)
t2 = testing(8)
print(t1.x, t2.x)
print(t1+t2)