import basic_math_and_functions as b

pi = b.pi_digits(100).pi

def taylorSeriesSine(x):
    term_1 = x
    term_2 = term_1 - ((x**3)/b.factorial(3))
    term_3 = term_2 + ((x**5)/b.factorial(5))
    term_4 = term_3 - ((x**7)/b.factorial(7))
    term_5 = term_4 + ((x**9)/b.factorial(9))
    term_6 = term_5 - ((x**11)/b.factorial(11))
    term_7 = term_6 + ((x**13)/b.factorial(13))

    return term_7

def sinRad(theta):
    theta = angleFixer(theta)
    if theta <= b.absolute_value(pi):
        return taylorSeriesSine(theta)
    
def angleFixer(theta):
    c = theta
    while c > b.absolute_value(pi):
        c -= (2*pi)
    return c

def cosRad(theta):
    cos = sinRad(theta + (pi/2))
    return cos

def tanRad(theta):
    tan = sinRad(theta) / cosRad(theta)
    return tan

def secRad(theta):
    sec = 1 / cosRad(theta)
    return sec

def cscRad(theta):
    csc = 1 / sinRad(theta)
    return csc

def cotRad(theta):
    cot = cosRad(theta) / sinRad(theta)
    return cot