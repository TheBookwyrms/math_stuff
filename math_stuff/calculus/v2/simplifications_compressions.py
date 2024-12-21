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
            c0 = compress_addition(tree.children[0])
            c1 = compress_addition(tree.children[1])
            two = node(operations.const, 2)
            one = node(operations.const, 1)
            tree = node(operations.operation, tree.arg, children=(c0, c1))
            if tree.arg == operations.add:
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


def compress_subtraction(tree: node):
    match tree.length():
        case 0:
            return tree
        case 1:
            tree = compress_subtraction(tree)
            return tree
        case 2:
            c0 = compress_subtraction(tree.children[0])
            c1 = compress_subtraction(tree.children[1])
            two = node(operations.const, 2)
            one = node(operations.const, 1)
            tree = node(operations.operation, tree.arg, children=(c0, c1))
            if tree.arg == operations.sub:
                if is_equal(c0, c1):
                    return node(operations.operation, operations.mult, children=(two, c0))
                if (c1.arg == operations.mult) and (c1.op == operations.operation):
                    if is_equal(c0, c1.children[0]):
                        return node(operations.operation, operations.mult, children=(c1.children[1]-one, c0))
                    elif is_equal(c0, c1.children[1]):
                        return node(operations.operation, operations.mult, children=(c1.children[0]-one, c0))
                if (c0.arg == operations.mult) and (c0.op == operations.operation):
                    if is_equal(c1, c0.children[0]):
                        return node(operations.operation, operations.mult, children=(c0.children[1]-one, c1))
                    elif is_equal(c1, c0.children[1]):
                        return node(operations.operation, operations.mult, children=(c0.children[0]-one, c1))
    return tree

def compress_to_power_one(tree: node):
    match tree.length():
        case 0:
            return tree
        case 1:
            tree = compress_to_power_one(tree)
            return tree
        case 2:
            child_0 = tree.children[0]
            child_1 = tree.children[1]
            child_0 = compress_to_power_one(child_0)
            child_1 = compress_to_power_one(child_1)
            tree = node(operations.operation, tree.arg, children=(child_0, child_1))

            if ((child_0.op == operations.operation) and (child_0.arg == operations.pow)) and not ((child_1.op == operations.operation) and (child_1.arg == operations.pow)):
                if (child_0.children[1].op == operations.const) and (child_0.children[1].arg == 1):
                    tree = node(operations.operation, tree.arg, children=(child_0.children[0], child_1))
            elif (child_1.op == operations.operation) and (child_1.arg == operations.pow) and not ((child_0.op == operations.operation) and (child_0.arg == operations.pow)):
                if (child_1.children[1].op == operations.const) and (child_1.children[1].arg == 1):
                    tree = node(operations.operation, tree.arg, children=(child_0, child_1.children[0]))
            elif ((child_0.op == operations.operation) and (child_0.arg == operations.pow)) and ((child_1.op == operations.operation) and (child_1.arg == operations.pow)):
                if ((child_0.children[1].op == operations.const) and (child_0.children[1].arg == 1)) and not ((child_1.children[1].op == operations.const) and (child_1.children[1].arg == 1)):
                    tree = node(operations.operation, tree.arg, children=(child_0.children[0], child_1))
                elif ((child_1.children[1].op == operations.const) and (child_1.children[1].arg == 1)) and not ((child_0.children[1].op == operations.const) and (child_0.children[1].arg == 1)):
                    tree = node(operations.operation, tree.arg, children=(child_0, child_1.children[0]))
                elif ((child_1.children[1].op == operations.const) and (child_1.children[1].arg == 1)) and ((child_0.children[1].op == operations.const) and (child_0.children[1].arg == 1)):
                    tree = node(operations.operation, tree.arg, children=(child_0.children[0], child_1.children[0]))
            
    return tree


def compress_constants(tree: node):
    match tree.length():
            case 0:
                return tree
            case 1:
                tree = compress_addition(tree)
                return tree
            case 2:
                c0 = compress_constants(tree.children[0])
                c1 = compress_constants(tree.children[1])
                tree = node(operations.operation, tree.arg, children=(c0, c1))
                if (c0.op == operations.const) and (c1.op == operations.const):
                    match tree.arg:
                        case operations.add:
                            tree = node(operations.const, c0.arg+c1.arg)
                            return tree
                        case operations.sub:
                            tree = node(operations.const, c0.arg-c1.arg)
                            return tree
                        case operations.mult:
                            tree = node(operations.const, c0.arg*c1.arg)
                            return tree
                        case operations.div:
                            tree = node(operations.const, c0.arg/c1.arg)
                            return tree
                        case operations.pow:
                            tree = node(operations.const, c0.arg**c1.arg)
                            return tree
                    raise ValueError("case error")
    return tree


def all_simplifications_and_compressions(tree: node):
    print(f'{colourer('31')}derived expression{colourer(0)}:        {tree}')
    tree = delete_Nones(tree)
    print(f'{colourer('35')}compressed Nones{colourer(0)}:          {tree}')
    tree = compress_addition(tree)
    print(f'{colourer('34')}compressed additions{colourer(0)}:      {tree}')
    tree = compress_subtraction(tree)
    print(f'{colourer('36')}compressed subtractions{colourer(0)}:   {tree}')
    tree = compress_constants(tree)
    print(f'{colourer('33')}compressed constants{colourer(0)}:      {tree}')
    tree = compress_to_power_one(tree)
    print(f'{colourer('32')}compressed powers{colourer(0)}:         {tree}')
    #return tree