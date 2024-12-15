def pi9():
    pi = 3.14159265
    return pi


def pi100():
    pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
    return pi


def absolute_value(x):
    if x >= 0:
        x = x
    if x < 0:
        x = x/(-1)
    
    return x


def factorial(x):
    x = x
    y = x
    while x >1:
        y = y * (x-1)
        x -= 1
    return y