from math_stuff.node_class import Node, subtypes, SubtypeException, operations, ChildrenException

class DifferentiabilityException(Exception):
    def __init__(self, *args):
        super().__init__(*args)


def derive_tree(tree:Node):

    if tree.subtype == subtypes.NULL:
        return Node(subtypes.NULL, None)
    elif tree.subtype == subtypes.CONSTANT:
        return Node(subtypes.NULL, None)
    elif tree.subtype == subtypes.NUMBER:
        return Node(subtypes.NULL, None)
    elif tree.subtype == subtypes.VAR:
        return Node(subtypes.VAR, tree.value+"'")
    elif tree.subtype == subtypes.OPERATION:
        match tree.value:
            case operations.ADD:
                derived_children = []
                for child in tree.children:
                    derived_children.append(derive_tree(child))

                return Node(subtypes.OPERATION, operations.ADD, children=tuple(derived_children))
            
            case operations.MULTIPLY:
                if len(tree.children)==2:
                    c0 = tree.children[0]
                    c0_derived = derive_tree(c0)
                    c1 = tree.children[1]
                    c1_derived = derive_tree(c1)
                    left = Node(subtypes.OPERATION, operations.MULTIPLY, children=(c0_derived, c1))
                    right = Node(subtypes.OPERATION, operations.MULTIPLY, children=(c0, c1_derived))
                    total = Node(subtypes.OPERATION, operations.ADD, children=(left, right))
                    return total
                elif len(tree.children)>2:
                    c_left = tree.children[0]
                    c_left_derived = derive_tree(c_left)
                    c_else = Node(subtypes.OPERATION, operations.MULTIPLY, children=tuple(tree.children[1:]))
                    c_else_derived = derive_tree(c_else)
                    left = Node(subtypes.OPERATION, operations.MULTIPLY, children=(c_left_derived, c_else))
                    right = Node(subtypes.OPERATION, operations.MULTIPLY, children=(c_left, c_else_derived))
                    total = Node(subtypes.OPERATION, operations.ADD, children=(left, right))
                    return total
                else:
                    raise ChildrenException(f'multiplication should not have {len(tree.children)} children')
            
            case operations.SUBTRACT:
                c0_derived = derive_tree(tree.children[0])
                c1_derived = derive_tree(tree.children[1])
                return Node(subtypes.OPERATION, operations.SUBTRACT, children=(c0_derived, c1_derived))

            case operations.DIVIDE:
                c0_derived = derive_tree(tree.children[0])
                c1_derived = derive_tree(tree.children[1])
                return Node(subtypes.OPERATION, operations.DIVIDE, children=(c0_derived, c1_derived))

            case operations.FLOOR_DIVISION:
                raise DifferentiabilityException(f"operation {tree.value} is not differentiable")
            
            case operations.MODULO_DIVISION:
                raise DifferentiabilityException(f"operation {tree.value} is not differentiable")
            
            case operations.POWER:
                pass
            
            case operations.LOG10:
                pass
            
            case operations.LN:
                pass
            
            case operations.SIN:
                pass
            
            case operations.COS:
                pass
            
            case operations.TAN:
                pass
            
            case operations.CSC:
                pass
            
            case operations.SEC:
                pass
            
            case operations.COT:
                pass
            
            case operations.ARCSIN:
                pass
            
            case operations.ARCCOS:
                pass
            
            case operations.ARCTAN:
                pass
            
            case operations.ARCCSC:
                pass
            
            case operations.ARCSEC:
                pass
            
            case operations.ARCCOT:
                pass
            
            case operations.ABS:
                raise DifferentiabilityException(f"operation {tree.value} is not differentiable")
            
            case operations.FLOOR:
                raise DifferentiabilityException(f"operation {tree.value} is not differentiable")
            
            case operations.CEIL:
                raise DifferentiabilityException(f"operation {tree.value} is not differentiable")
    else:
        raise SubtypeException(f"subtype {tree.subtype} is not a supported Node subtype")
    

def run_2():

    five = Node(subtypes.NUMBER, 5)
    x = Node(subtypes.VAR, "x")
    y = Node(subtypes.VAR, "y")
    z = Node(subtypes.VAR, "z")
    a = Node(subtypes.VAR, "a")
    b = Node(subtypes.VAR, "b")
    c = Node(subtypes.VAR, "c")
    test = five+x+14
    m_test = x*y*z*a*b*c
    a2 = x+y+z+a+b+c
    print(a2.simplify_multiple_additions())
    mt2 = m_test.simplify_multiple_multiplications()
    mt4 = derive_tree(mt2)

    print(derive_tree(five), derive_tree(x))
    print(derive_tree(test).simplify_multiple_additions())
    print()
    print(m_test)
    print(mt2)
    print(mt4)


if __name__ == "__main__":
    run_2()