from math_stuff.calculus.v2.tree_builder_2 import *
from math_stuff.calculus.v2.is_equal import *

import copy

def substitute_var_as(tree, substitution_dict):
    original_tree = node(-0.01, 1)

    def actual_process(tree, substitution_dict):
        match tree.length():
            case 0:
                if tree.op == operations.var:
                    if tree.arg in substitution_dict:
                        tree.arg = substitution_dict[tree.arg]
            case 1:
                c = actual_process(tree.children, substitution_dict)

                tree = node(tree.op, tree.arg, children=(c))
            case 2:
                c0 = actual_process(tree.children[0], substitution_dict)
                c1 = actual_process(tree.children[1], substitution_dict)

                tree = node(tree.op, tree.arg, children=(c0, c1))
        return tree
        
    while not is_equal(original_tree, tree):
        original_tree = copy.deepcopy(tree)
        #print(original_tree, "a")
        tree = actual_process(tree, substitution_dict)
        #print(original_tree, "b")
        #print(f'{original_tree},\n{tree},\n{is_equal(original_tree, tree)}')
        #print()
    
    return tree