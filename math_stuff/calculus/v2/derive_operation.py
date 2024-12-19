from math_stuff.calculus.v2.tree_builder_2 import *


def derive_operation(parent: node):
    if parent.op == "operation_type":
        match parent.arg:
            case operations.add:
                left = derive_operation(parent.children[0])
                right = derive_operation(parent.children[1])

                new_parent = node("operation_type", operations.add, children=(left, right))

                return new_parent
            case operations.sub:
                left = derive_operation(parent.children[0])
                right = derive_operation(parent.children[1])

                new_parent = node("operation_type", operations.sub, children=(left, right))

                return new_parent
            case operations.mult:
                a = parent.children[0]
                b = parent.children[1]
                aa = derive_operation(a)
                bb = derive_operation(b)
                #aa.is_differentiable = True
                #bb.is_differentiable = True

                new_child_1 = node("operation_type", operations.mult,
                children=(aa, b))

                new_child_2 = node("operation_type", operations.mult,
                children=(a, bb))

                new_parent = node("operation_type", operations.add,
                children=(new_child_1, new_child_2))



                return new_parent
            case operations.div:
                a = parent.children[0]
                b = parent.children[1]
                aa = derive_operation(a)
                bb = derive_operation(b)
                two = node("const", 2)

                top_a = node("operation_type", operations.mult, children=(aa, b))
                top_b = node("operation_type", operations.mult, children=(a, bb))
                top = node("operation_type", operations.sub, children=(top_a, top_b))
                bottom = node("operation_type", operations.pow, children=(b, two))
                division = node("operation_type", operations.div, children=(top, bottom))

                return division
            case 14:
                if parent.children[1].op == "const":
                    one = node("const", 1)
                    u = parent.children[0]
                    to_the_n = parent.children[1]

                    new_base_power = node("operation_type", operations.pow
                                          , children=(u, to_the_n-one))

                    front__power = node("operation_type", operations.mult
                    , children=(to_the_n, new_base_power))

                    u_prime = derive_operation(u)

                    with_u_prime = node("operation_type", operations.mult
                    , children=(front__power, u_prime))

                    return with_u_prime
                else:
                    f_x = parent
                    g_x = parent.children[0]
                    h_x = parent.children[1]
                    g_prime = derive_operation(g_x)
                    h_prime = derive_operation(h_x)

                    ln_g_x = node("operation_type", operations.ln, children=(g_x))
                    ln_g_x_prime = derive_operation(ln_g_x)

                    term_1 = node("operation_type", operations.mult, children=(h_prime, ln_g_x))
                    term_2 = node("operation_type", operations.mult, children=(h_x, ln_g_x_prime))
                    add = term_1 + term_2

                    final = node("operation_type", operations.mult, children=(f_x, add))

                    return final
            case 15:
                u = parent.children
                u_prime = derive_operation(u)

                div = u_prime/u

                return div
            case 21:
                pass
            case 22:
                pass
            case 23:
                pass
            case 24:
                pass
            case 25:
                pass
            case 26:
                pass
            case 31:
                pass
            case 32:
                pass
            case 33:
                pass
            case 34:
                pass
            case 35:
                pass
            case 36:
                pass
    elif parent.op == ("const" or "void"):
        a = node("void", None)
        return a
    elif parent.op == "var":
        var_prime = node("var", f"{parent.arg}'")

        var_var_prime = node("operation_type", operations.mult,
        children=(parent, var_prime))

        return var_prime
    else:
        print()