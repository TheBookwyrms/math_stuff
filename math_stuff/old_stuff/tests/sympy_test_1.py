import numpy as np
from sympy import *

x, y, z = symbols('x, y, z')
a = (diff(cos(x), x))
def b(xx):
    return (diff(cos(xx), x))


def parser(text):
    return parse_expr(text)

def eval_for_values(func, *nums):
    substitutions = {}
    for num, variable in zip(nums, ["x", "y", "z"]):
        substitutions[variable] = num
    
    return func.evalf(subs=substitutions)

#values = {x:3, y:4}

func = parser("cos(x) + sin(y)")
#a = (t1.subs([[x, 2], [y, 3]]))
#print(func.evalf(subs=values))
print(eval_for_values(func, 3, 4, 0)) # x, y, z