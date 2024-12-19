from math_stuff.calculus.v2.tree_builder_2 import *

def compress_Nones(tree: node):
    match tree.length():
        case 0:
            return tree
        case 1:
            return tree
        case 2:
            tree = node(tree.op, tree.arg, children=(
                compress_Nones(tree.children[0]),
                compress_Nones(tree.children[1])
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