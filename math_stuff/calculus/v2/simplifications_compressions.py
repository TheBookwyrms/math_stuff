from math_stuff.calculus.v2.tree_builder_2 import *

import time

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
            t = compress_addition(tree.children)
            tree = node(tree.op, tree.arg, children=(t))
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
            t = compress_subtraction(tree.children)
            tree = node(tree.op, tree.arg, children=(t))
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
            t = compress_to_power_one(tree.children)
            tree = node(tree.op, tree.arg, children=(t))
            return tree
        case 2:
            child_0 = tree.children[0]
            child_1 = tree.children[1]
            child_0 = compress_to_power_one(child_0)
            child_1 = compress_to_power_one(child_1)
            tree = node(operations.operation, tree.arg, children=(child_0, child_1))
            one = node(operations.const, 1)


            if ((child_0.op == operations.operation) and (child_0.arg == operations.pow)) and not ((child_1.op == operations.operation) and (child_1.arg == operations.pow)):
                if is_equal(child_0.children[1], one):
                    tree = node(operations.operation, tree.arg, children=(child_0.children[0], child_1))
            elif (child_1.op == operations.operation) and (child_1.arg == operations.pow) and not ((child_0.op == operations.operation) and (child_0.arg == operations.pow)):
                if is_equal(child_1.children[1], one):
                    tree = node(operations.operation, tree.arg, children=(child_0, child_1.children[0]))
            elif ((child_0.op == operations.operation) and (child_0.arg == operations.pow)) and ((child_1.op == operations.operation) and (child_1.arg == operations.pow)):
                if (is_equal(child_0.children[1], one)) and not (is_equal(child_1.children[1], one)):
                    tree = node(operations.operation, tree.arg, children=(child_0.children[0], child_1))
                elif (is_equal(child_1.children[1], one)) and not (is_equal(child_0.children[1], one)):
                    tree = node(operations.operation, tree.arg, children=(child_0, child_1.children[0]))
                elif (is_equal(child_1.children[1], one)) and (is_equal(child_0.children[1], one)):
                    tree = node(operations.operation, tree.arg, children=(child_0.children[0], child_1.children[0]))
            
    return tree

def remove_mult_div_by_one(tree: node):
    match tree.length():
        case 0:
            return tree
        case 1:
            t = remove_mult_div_by_one(tree.children)
            tree = node(tree.op, tree.arg, children=(t))
            return tree
        case 2:
            child_0 = tree.children[0]
            child_1 = tree.children[1]
            child_0 = remove_mult_div_by_one(child_0)
            child_1 = remove_mult_div_by_one(child_1)
            tree = node(operations.operation, tree.arg, children=(child_0, child_1))
            one = node(operations.const, 1)
            
            #if (tree.op == operations.operation):
            #    if (tree.arg == operations.mult):
            #        if is_equal(tree.children[0], one):
            #            return tree.children[1]
            #        elif is_equal(tree.children[1], one):
            #            return tree.children[0]
            #    elif (tree.arg == operations.div):
            #        if is_equal(tree.children[1], one):
            #            return tree.children[0]
            
            if (tree.op == operations.operation) and ((tree.arg == operations.mult) or (tree.arg == operations.div)):
                if is_equal(tree.children[1], one):
                        return tree.children[0]
            elif (tree.op == operations.operation) and (tree.arg == operations.mult):
                    if is_equal(tree.children[0], one):
                        return tree.children[1]

    return tree


def compress_constants(tree: node):
    match tree.length():
            case 0:
                return tree
            case 1:
                t = compress_addition(tree.children)
                tree = node(tree.op, tree.arg, children=(t))
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


def compress_repeated_multiplication(tree: node):
    match tree.length():
        case 0:
            return tree
        case 1:
            t=compress_repeated_multiplication(tree.children)
            tree = node(tree.op, tree.arg, children=(t))
            return tree
        case 2:
            c0 = compress_repeated_multiplication(tree.children[0])
            c1 = compress_repeated_multiplication(tree.children[1])
            tree = node(operations.operation, tree.arg, children=(c0, c1))

            
            one = node(operations.const, 1)
            two = node(operations.const, 2)

            if (tree.op == operations.operation) and (tree.arg == operations.mult):
                if is_equal(tree.children[0], tree.children[1]):
                    return node(operations.operation, operations.pow, children=(tree.children[0], two))
                
                elif (tree.children[0].op == operations.operation) and (tree.children[0].arg == operations.pow):
                    if is_equal(tree.children[0].children[0], tree.children[1]):
                        return node(operations.operation, operations.pow, children=(tree.children[1], tree.children[0].children[1]+one))

                elif (tree.children[1].op == operations.operation) and (tree.children[1].arg == operations.pow):
                    if is_equal(tree.children[1].children[0], tree.children[0]):
                        return node(operations.operation, operations.pow, children=(tree.children[0], tree.children[1].children[1]+one))

                elif (tree.children[0].op == operations.operation) and (tree.children[0].arg == operations.pow) and (tree.children[1].op == operations.operation) and (tree.children[1].arg == operations.pow):
                    if is_equal(tree.children[0].children[0], tree.children[1].children[0]):
                        return node(operations.operation, operations.pow, children=(
                            tree.children[0].children[0],
                            tree.children[0].children[1]+tree.children[1].children[1]
                        ))
    return tree


def separate_pow_with_mult_div_to_compress(tree: node):
    match tree.length():
        case 0:
            return tree
        case 1:
            t=separate_pow_with_mult_div_to_compress(tree.children)
            tree = node(tree.op, tree.arg, children=(t))
            return tree
        case 2:
            c0 = separate_pow_with_mult_div_to_compress(tree.children[0])
            c1 = separate_pow_with_mult_div_to_compress(tree.children[1])
            tree = node(operations.operation, tree.arg, children=(c0, c1))

            if (tree.op == operations.operation) and (tree.arg == operations.pow):
                if (tree.children[0].op == operations.operation) and (
                    (tree.children[0].arg == operations.mult) or
                    (tree.children[0].arg == operations.div)
                    ):
                    return node(
                        operations.operation,
                        tree.children[0].arg,
                        children=(
                            tree.children[0].children[0]**tree.children[1],
                            tree.children[0].children[1]**tree.children[1],
                        )
                    )
    return tree


def compress_pow_to_pow(tree: node):
    match tree.length():
        case 0:
            return tree
        case 1:
            t=compress_pow_to_pow(tree.children)
            tree = node(tree.op, tree.arg, children=(t))
            return tree
        case 2:
            c0 = compress_pow_to_pow(tree.children[0])
            c1 = compress_pow_to_pow(tree.children[1])
            tree = node(operations.operation, tree.arg, children=(c0, c1))

            if (tree.op == operations.operation) and (tree.arg == operations.pow):
                if (tree.children[0].op == operations.operation) and (tree.children[0].arg == operations.pow):
                    return node(
                        operations.operation,
                        operations.pow,
                        children=(
                            tree.children[0].children[0],
                            tree.children[0].children[1]*tree.children[1]
                        )
                    )
    return tree


def distribute_mult(tree:node):
    match tree.length():
        case 0:
            return tree
        case 1:
            return distribute_mult(tree.children)
        case 2:
            c0 = distribute_mult(tree.children[0])
            c1 = distribute_mult(tree.children[1])
            tree = node(operations.operation, tree.arg, children=(c0, c1))

                
            if (tree.op == operations.operation) and (tree.arg == operations.mult):

                if (
                    ((tree.children[0].length() == 0) or (tree.children[0].length() == 1)) and
                    (tree.children[1].length() == 2)):
                    '''
                    (a) * (b±c) = (a*b) ± (a*c)
                    '''
                    c1_arg = tree.children[1].arg

                    left = tree.children[0] * tree.children[1].children[0]
                    right = tree.children[0] * tree.children[1].children[1]

                    return node(operations.operation, c1_arg, children=(left, right))
                    pass
                elif (
                    ((tree.children[1].length() == 0) or (tree.children[1].length() == 1)) and
                    (tree.children[0].length() == 2)):
                    '''
                    (a±b) * (c) = (a*c) ± (b*c)
                    '''
                    c0_arg = tree.children[0].arg

                    left = tree.children[0].children[0] * tree.children[1]
                    right = tree.children[0].children[1] * tree.children[1]

                    return node(operations.operation, c0_arg, children=(left, right))
                    pass
                elif (
                    (tree.children[0].length() == 2) and
                    (tree.children[1].length() == 2)):
                    '''
                    ° = ±
                    ' = ±
                    (a°b) * (c'd) = (a*c) + (a*'d) + (°b*c) + (°b*'d)
                    '''

                    c0_arg = tree.children[0].arg
                    c1_arg = tree.children[1].arg
                    
                    a = tree.children[0].children[0]
                    b = tree.children[0].children[1]
                    c = tree.children[1].children[0]
                    d = tree.children[1].children[1]

                    negative_one = node(operations.const, -1)

                    term_1 = a * c
                    term_2 = a * d if c1_arg == operations.add else a * d * negative_one
                    term_3 = b * c if c0_arg == operations.add else b * c * negative_one
                    term_4 = b * d if c0_arg == c1_arg else b * c * negative_one

                    return term_1 + term_2 + term_3 + term_4
                    
                    pass
                pass

    return tree


def all_simplifications_and_compressions(tree: node):
    original_tree = node(0, 1)
    while not is_equal(original_tree, tree):
        original_tree = tree
        tree = delete_Nones(tree)
        tree = compress_addition(tree)
        tree = compress_subtraction(tree)
        tree = compress_constants(tree)
        tree = compress_to_power_one(tree)
        tree = remove_mult_div_by_one(tree)
        tree = compress_repeated_multiplication(tree)
        tree = separate_pow_with_mult_div_to_compress(tree)
    #print()
    #print(tree)
    #print()
    #tree = distribute_mult(tree)

    return tree