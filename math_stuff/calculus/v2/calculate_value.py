from math_stuff.calculus.v2.tree_builder_2 import *

import numpy as np

basic_numpy = {
    15: np.log,
    21: np.sin,
    22: np.cos,
    23: np.cos,
    31: np.asin,
    32: np.acos,
    33: np.atan,
    41: np.floor,
    42: np.ceil,
    45: np.abs
}

inverse_not_really_trig = {
    24: np.cos,
    25: np.sin,
    26: np.tan,
}

arctrig = {
    34: np.acos,
    35: np.asin,
    36: np.atan,
}


basic_operators = {
    8: np.add,
    9: np.subtract,
    10: np.multiply,
    11: np.divide,
    14: np.power,
}


def calculate_value_of(tree: node):
    match tree.length():
        case 0:
            if tree.op != operations.const:
                raise ValueError(f'{reverser[tree.op]} is not constant')
            return tree
        case 1:
            c = calculate_value_of(tree.children)
            if tree.arg in basic_numpy:
                tree = basic_numpy[tree.arg](c.arg)
            elif tree.arg in inverse_not_really_trig:
                tree = 1/inverse_not_really_trig[tree.arg](c.arg)
            elif tree.arg in arctrig:
                tree = arctrig[tree.arg](1/c.arg)
            else:
                raise ValueError("invalid operation")
            return tree

        case 2:
            c0 = calculate_value_of(tree.children[0])
            c1 = calculate_value_of(tree.children[1])

            if tree.arg in basic_operators:
                tree = basic_operators[tree.arg](c0, c1)
            else:
                raise ValueError("invalid operation")
            return tree
    
    raise ValueError("case error")