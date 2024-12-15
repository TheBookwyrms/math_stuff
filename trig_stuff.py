import basic_math_and_functions as b

def taylorSeriesSine(x):
    term_1 = x
    term_2 = term_1 - ((x**3)/b.factorial(3))
    term_3 = term_2 + ((x**5)/b.factorial(5))
    term_4 = term_3 - ((x**7)/b.factorial(7))
    term_5 = term_4 + ((x**9)/b.factorial(9))

    return term_5

def sinRad(theta):
    theta = angleFixer(theta)
    if theta <= b.absolute_value(b.pi9()):
        return taylorSeriesSine(theta)

def angleFixer(theta):
    while theta > b.absolute_value(b.pi9()):
        theta -= (2*b.pi9())
    return theta

def cosRad(theta):
    cos = sinRad(theta + (b.pi9()/2))
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