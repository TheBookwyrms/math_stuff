#def sin(u):
#    return [0,u]

def cos(u):
    return [1,u]
def sin(u):
    return [0,u]

class int:
    def __init__(self, val):
        self.val = [val]

def __add__(a, b):
    a = [a]
    return [a, -1, b]

[1, [0, [1, [3]]]]

print(int(2).val)
print(eval("sin(2)"))
print(eval("'x'"))
print(eval("cos('x')"))
print(eval("sin(cos('x'))"))
print(eval("cos(sin(cos('x')))"))
print(eval("cos(sin(cos(3))) + int(2).val"))