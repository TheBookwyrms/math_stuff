class pi_digits:
    def __init__(self, num):
        if (num > 100) or (num < 0) or (type(num) != int):
            raise ValueError("pi: 0 to 100 digits, int")
        
        pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
        self.pi = float(pi[:num+2])

def absolute_value(x):
    if x >= 0:
        x = x
    if x < 0:
        x = x/(-1)
    
    return x

def factorial(x):

    # NOTE : 0! should = 1

    x = x
    y = x
    while x >1:
        y = y * (x-1)
        x -= 1
    return y

for i in range(10):
    print(factorial(i))