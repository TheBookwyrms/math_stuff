from math_stuff.calculus.v2.tree_builder_2 import *

def delete_Nones(tree: node):
    match tree.length():
        case 0:
            return tree
        case 1:
            if tree.op == operations.operation:
                if tree.children.op == operations.void:
                    tree.op = operations.void
                    tree.arg = None
                    tree.children = []
            return tree
        case 2:
            tree = node(tree.op, tree.arg, children=(
                delete_Nones(tree.children[0]),
                delete_Nones(tree.children[1])
            ))
            if (tree.op == operations.operation) and ((tree.arg == 10) or (tree.arg == 11)):
                if (tree.children[0].op == operations.void) or (tree.children[1].op == operations.void):
                    tree.op = operations.void
                    tree.arg = None
                    tree.children = []
            if (tree.op == operations.operation) and ((tree.arg == 8) or (tree.arg == 9)):
                if (tree.children[0].op == operations.void) and (tree.children[1].op == operations.void):
                    tree.op = operations.void
                    tree.arg = None
                    tree.children = []
                elif (tree.children[0].op == operations.void) and (tree.children[1].op != operations.void):
                    tree = tree.children[1]
                elif (tree.children[0].op != operations.void) and (tree.children[1].op == operations.void):
                    tree = tree.children[0]
            return tree
    raise ValueError("error")


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

def compress_addition(tree: node):
    match tree.length():
        case 0:
            return tree
        case 1:
            tree = compress_addition(tree)
            return tree
        case 2:
            if tree.arg == operations.add:
                c0 = compress_addition(tree.children[0])
                c1 = compress_addition(tree.children[1])
                two = node(operations.const, 2)
                one = node(operations.const, 1)
                tree = node(operations.operation, operations.add, children=(c0, c1))
                if is_equal(c0, c1):
                    return node(operations.operation, operations.mult, children=(two, c0))
                if (c1.arg == operations.mult) and (c1.op == operations.operation):
                    if is_equal(c0, c1.children[0]):
                        return node(operations.operation, operations.mult, children=(c1.children[1]+one, c0))
                    elif is_equal(c0, c1.children[1]):
                        return node(operations.operation, operations.mult, children=(c1.children[0]+one, c0))
                if (c0.arg == operations.mult) and (c0.op == operations.operation):
                    if is_equal(c1, c0.children[0]):
                        return node(operations.operation, operations.mult, children=(c0.children[1]+one, c1))
                    elif is_equal(c1, c0.children[1]):
                        return node(operations.operation, operations.mult, children=(c0.children[0]+one, c1))
    return tree


def all_simplifications_and_compressions(tree: node):
    tree = delete_Nones(tree)
    tree = compress_addition(tree)
    return tree