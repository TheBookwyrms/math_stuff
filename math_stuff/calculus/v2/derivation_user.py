from math_stuff.calculus.v2.tree_builder_2 import *
from math_stuff.calculus.v2.derive_operation import *
from math_stuff.calculus.v2.simplifications_compressions import *


def run():
    o = node(operations.const, 1)
    ono = node(operations.const, 1)
    t = node(operations.const, 2)
    th = node(operations.const, 3)
    f = node(operations.const, 4)
    fi = node(operations.const, 5)
    _s = node(operations.const, -7)
    x = node(operations.var, "x")
    x_p = node(operations.var, "x'")

    ch = o/(th*(x**th))
    ch = (th*(x**t))/(x*x*x*t)
    ch = x**t+x**t+x**t+x**t
    #ch = sec(csc(x**x))
    #ch = ln(t)
    #ch = x**(ln(x))
    #ch = o*t+(x**t)
    #ch = (x*x*x*t)
    #ch = ch+fi
    t = derive_operation(ch)

    print()
    print(f'original expression:    {ch}')
    print(f'derived expression:     {t}')
    print(f'compressed expression:  {all_simplifications_and_compressions(t)}')
    print()
    print(is_equal(x**t+x**t, x**t+x**t))