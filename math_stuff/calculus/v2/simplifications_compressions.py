from math_stuff.calculus.v2.tree_builder_2 import *

def delete_Nones(tree: node):
    match tree.length():
        case 0:
            return tree
        case 1:
            if tree.op == "operation_type":
                if tree.children.op == "void":
                    tree.op = "void"
                    tree.arg = None
                    tree.children = []
            return tree
        case 2:
            tree = node(tree.op, tree.arg, children=(
                delete_Nones(tree.children[0]),
                delete_Nones(tree.children[1])
            ))
            if (tree.op == "operation_type") and ((tree.arg == 10) or (tree.arg == 11)):
                if (tree.children[0].op == "void") or (tree.children[1].op == "void"):
                    tree.op = "void"
                    tree.arg = None
                    tree.children = []
            if (tree.op == "operation_type") and ((tree.arg == 8) or (tree.arg == 9)):
                if (tree.children[0].op == "void") and (tree.children[1].op == "void"):
                    tree.op = "void"
                    tree.arg = None
                    tree.children = []
                elif (tree.children[0].op == "void") and (tree.children[1].op != "void"):
                    tree = tree.children[1]
                elif (tree.children[0].op != "void") and (tree.children[1].op == "void"):
                    tree = tree.children[0]
            return tree
    raise ValueError("error")


def compress_duplicate_additions_or_subtractions(tree: node):
    match tree.length():
        case 0:
            return tree
        case 1:
            tree = compress_duplicate_additions_or_subtractions(tree)
            return tree
        case 2:
            if (tree.op == "operation_type") and ((tree.arg == 8) or (tree.arg == 9)):
                new_tree_0 = compress_duplicate_additions_or_subtractions(tree.children[0])
                new_tree_1 = compress_duplicate_additions_or_subtractions(tree.children[1])

                tree = node("operation_type", tree.arg, children=(new_tree_0, new_tree_1))

                if is_equal(tree.children[0], tree.children[1]):
                    two = node("const", 2)
                    tree = node("operation_type", operations.mult, children=(two, tree.children[0]))
            return tree
    raise ValueError("case error")


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


def all_simplifications_and_compressions(tree: node):
    tree = delete_Nones(tree)
    tree = compress_duplicate_additions_or_subtractions(tree)
    return tree