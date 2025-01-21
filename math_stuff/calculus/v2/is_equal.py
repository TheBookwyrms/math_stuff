from math_stuff.calculus.v2.tree_builder_2 import *


def is_equal(tree_1: node, tree_2: node):
    length_1 = tree_1.length()
    length_2 = tree_2.length()

    if length_1 == length_2:
        match length_1:
            case 0:
                if (tree_1.op == tree_2.op) and (tree_1.arg == tree_2.arg):
                    return True
                return False
            case 1:
                if (tree_1.op == tree_2.op) and (tree_1.arg == tree_2.arg):
                    if is_equal(tree_1.children, tree_2.children):
                        return True
                return False
            case 2:
                if (tree_1.op == tree_2.op) and (tree_1.arg == tree_2.arg):
                    if is_equal(tree_1.children[0], tree_2.children[0]):
                        if is_equal(tree_1.children[1], tree_2.children[1]):
                            return True
                    elif is_equal(tree_1.children[0], tree_2.children[1]):
                        if is_equal(tree_1.children[1], tree_2.children[0]):
                            return True
                return False
        raise ValueError("case error")

    return False