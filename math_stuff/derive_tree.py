from math_stuff.node_class import *

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
                f = tree
                g = tree.children[0]
                g_prime = derive_tree(g)
                h = tree.children[1]
                h_prime = derive_tree(h)

                '''
                f = g**h
                ln(f) = h*ln(g)
                f'/f = h'*ln(g) + h*g'/g
                f'(x) = f(x) * (h'(x) * ln(g(x)) + h(x) * g'(x) / g(x))
                '''

                f_prime = f * ((h_prime * ln(g)) + (h * g_prime / g))

                return f_prime
            
            case operations.LOG10:
                g = tree.children[0]
                g_prime = derive_tree(g)
                ten = Node(subtypes.NUMBER, 10)

                return g_prime / (g * ln(ten))
            
            case operations.LN:
                g = tree.children[0]
                g_prime = derive_tree(g)

                return g_prime / g
            
            case operations.SIN:
                g = tree.children[0]
                g_prime = derive_tree(g)

                return cos(g)*g_prime

            case operations.COS:
                g = tree.children[0]
                g_prime = derive_tree(g)
                negative_one = Node(subtypes.NUMBER, -1)

                return negative_one*sin(g)*g_prime
            
            case operations.TAN:
                g = tree.children[0]
                g_prime = derive_tree(g)
                two = Node(subtypes.NUMBER, 2)

                return (sec(g)**two) * g_prime
            
            case operations.CSC:
                g = tree.children[0]
                g_prime = derive_tree(g)
                negative_one = Node(subtypes.NUMBER, -1)

                return negative_one * csc(g) * cot(g) * g_prime
            
            case operations.SEC:
                g = tree.children[0]
                g_prime = derive_tree(g)

                return sec(g) * tan(g) * g_prime
            
            case operations.COT:
                g = tree.children[0]
                g_prime = derive_tree(g)
                two = Node(subtypes.NUMBER, 2)
                negative_one = Node(subtypes.NUMBER, -1)

                return negative_one * (csc(g)**two) * g_prime
            
            case operations.ARCSIN:
                g = tree.children[0]
                g_prime = derive_tree(g)
                one = Node(subtypes.NUMBER, 1)
                half = Node(subtypes.NUMBER, 0.5)
                two = Node(subtypes.NUMBER, 2)

                return g_prime / ((one - g**two)**half)
            
            case operations.ARCCOS:
                g = tree.children[0]
                g_prime = derive_tree(g)
                one = Node(subtypes.NUMBER, 1)
                half = Node(subtypes.NUMBER, 0.5)
                two = Node(subtypes.NUMBER, 2)
                negative_one = Node(subtypes.NUMBER, -1)

                return negative_one * g_prime / ((one - g**two)**half)
            
            case operations.ARCTAN:
                g = tree.children[0]
                g_prime = derive_tree(g)
                one = Node(subtypes.NUMBER, 1)
                two = Node(subtypes.NUMBER, 2)

                return g_prime / (one + g**two)
            
            case operations.ARCCSC:
                g = tree.children[0]
                g_prime = derive_tree(g)
                one = Node(subtypes.NUMBER, 1)
                two = Node(subtypes.NUMBER, 2)
                negative_one = Node(subtypes.NUMBER, -1)

                return negative_one * g_prime / (abs(g) * (g**two - 1)**half)
            
            case operations.ARCSEC:
                g = tree.children[0]
                g_prime = derive_tree(g)
                one = Node(subtypes.NUMBER, 1)
                two = Node(subtypes.NUMBER, 2)

                return g_prime / (abs(g) * (g**two - 1)**half)
            
            case operations.ARCCOT:
                g = tree.children[0]
                g_prime = derive_tree(g)
                one = Node(subtypes.NUMBER, 1)
                two = Node(subtypes.NUMBER, 2)
                negative_one = Node(subtypes.NUMBER, -1)

                return negative_one * g_prime / (one + g**two)
            
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

    a3 = ((x**y) * (a*b))
    a4 = tan(a3)
    #print("   ", a3)
    #print(a4)
    #print("                           ", derive_tree(a3))
    #print(derive_tree(a4))

    #print(a2.simplify_multiple_additions())
    #mt2 = m_test.simplify_multiple_multiplications()
    #mt4 = derive_tree(mt2)

    subs_dict = {
        "a":5,
    }
    print(a4)
    print(a4.sub_variables(subs_dict))

    #print(derive_tree(five), derive_tree(x))
    #print(derive_tree(test).simplify_multiple_additions())
    #print()
    #print(m_test)
    #print(mt2)
    #print(mt4)


if __name__ == "__main__":
    run_2()