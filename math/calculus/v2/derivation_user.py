from math.calculus.v2.tree_builder_2 import *
from math.calculus.v2.derive_operation import *
from math.calculus.v2.simplifications_compressions import *


def run():
    o = node("const", 1)
    t = node("const", 2)
    th = node("const", 3)
    f = node("const", 4)
    fi = node("const", 5)
    _s = node("const", -7)
    x = node("var", "x")

    ch = o/(th*(x**th))
    ch = (th*(x**t))/(x*x*x*t)
    #ch = x**(ln(x))
    ch = o*t+(x**t)
    #ch = (x*x*x*t)
    #ch = ch+fi
    t = derive_operation(ch)



    print()
    print(f'original expression:    {ch}')
    print(f'derived expression:     {t}')
    print(f'compressed expression:  {compress_Nones(t)}')
    print()