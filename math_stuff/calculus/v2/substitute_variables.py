from math_stuff.calculus.v2.tree_builder_2 import *

def substitute_var_as(tree, substitution_dict):
    match tree.length():
        case 0:
            if tree.op == operations.var:
                if tree.arg in substitution_dict:
                    tree.arg = substitution_dict[tree.arg]
            return tree
        case 1:
            c = substitute_var_as(tree.children, substitution_dict)

            tree = node(tree.op, tree.arg, children=(c))
            return tree

        case 2:
            c0 = substitute_var_as(tree.children[0], substitution_dict)
            c1 = substitute_var_as(tree.children[1], substitution_dict)

            tree = node(tree.op, tree.arg, children=(c0, c1))
            return tree

    raise ValueError("error")