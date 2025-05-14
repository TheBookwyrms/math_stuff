from math_stuff.calculus.v2.tree_builder_2 import *


def derive_operation(parent: node, with_respect_to="all"):
    if parent.op == operations.operation:
        match parent.arg:
            case operations.add:
                left = derive_operation(parent.children[0], with_respect_to=with_respect_to)
                right = derive_operation(parent.children[1], with_respect_to=with_respect_to)

                new_parent = node(operations.operation, operations.add, children=(left, right))

                return new_parent
            case operations.sub:
                left = derive_operation(parent.children[0], with_respect_to=with_respect_to)
                right = derive_operation(parent.children[1], with_respect_to=with_respect_to)

                new_parent = node(operations.operation, operations.sub, children=(left, right))

                return new_parent
            case operations.mult:
                a = parent.children[0]
                b = parent.children[1]
                aa = derive_operation(a, with_respect_to=with_respect_to)
                bb = derive_operation(b, with_respect_to=with_respect_to)
                #aa.is_differentiable = True
                #bb.is_differentiable = True

                new_child_1 = node(operations.operation, operations.mult,
                children=(aa, b))

                new_child_2 = node(operations.operation, operations.mult,
                children=(a, bb))

                new_parent = node(operations.operation, operations.add,
                children=(new_child_1, new_child_2))



                return new_parent
            case operations.div:
                a = parent.children[0]
                b = parent.children[1]
                aa = derive_operation(a, with_respect_to=with_respect_to)
                bb = derive_operation(b, with_respect_to=with_respect_to)
                two = node(operations.const, 2)

                top_a = node(operations.operation, operations.mult, children=(aa, b))
                top_b = node(operations.operation, operations.mult, children=(a, bb))
                top = node(operations.operation, operations.sub, children=(top_a, top_b))
                bottom = node(operations.operation, operations.pow, children=(b, two))
                division = node(operations.operation, operations.div, children=(top, bottom))

                return division
            case operations.pow:
                if parent.children[1].op == operations.const:
                    one = node(operations.const, 1)
                    u = parent.children[0]
                    to_the_n = parent.children[1]

                    new_base_power = node(operations.operation, operations.pow
                                          , children=(u, to_the_n-one))

                    front__power = node(operations.operation, operations.mult
                    , children=(to_the_n, new_base_power))

                    u_prime = derive_operation(u, with_respect_to=with_respect_to)

                    with_u_prime = node(operations.operation, operations.mult
                    , children=(front__power, u_prime))

                    return with_u_prime
                else:
                    f_x = parent
                    g_x = parent.children[0]
                    h_x = parent.children[1]
                    g_prime = derive_operation(g_x, with_respect_to=with_respect_to)
                    h_prime = derive_operation(h_x, with_respect_to=with_respect_to)

                    ln_g_x = node(operations.operation, operations.ln, children=(g_x))
                    ln_g_x_prime = derive_operation(ln_g_x, with_respect_to=with_respect_to)

                    term_1 = node(operations.operation, operations.mult, children=(h_prime, ln_g_x))
                    term_2 = node(operations.operation, operations.mult, children=(h_x, ln_g_x_prime))
                    add = term_1 + term_2

                    final = node(operations.operation, operations.mult, children=(f_x, add))

                    return final
            case operations.ln:
                u = parent.children
                u_prime = derive_operation(u, with_respect_to=with_respect_to)

                try:
                    div = u_prime/u
                except:
                    div = node(operations.void, None)

                return div
            case operations.sin:
                u = parent.children
                u_prime = derive_operation(u, with_respect_to=with_respect_to)
                return cos(u)*u_prime
            
            case operations.cos:
                u = parent.children
                u_prime = derive_operation(u, with_respect_to=with_respect_to)
                minus_one = node(operations.const, -1)
                return minus_one*sin(u)*u_prime
                
            case operations.tan:
                u = parent.children
                u_prime = derive_operation(u, with_respect_to=with_respect_to)
                two = node(operations.const, 2)
                return ((sec(u))**two)*u_prime
            
            case operations.sec:
                u = parent.children
                u_prime = derive_operation(u, with_respect_to=with_respect_to)
                return sec(u)*tan(u)*u_prime
            
            case operations.csc:
                u = parent.children
                u_prime = derive_operation(u, with_respect_to=with_respect_to)
                two = node(operations.const, 2)
                minus_one = node(operations.const, -1)
                return minus_one*csc(u)*cot(u)*u_prime
            
            case operations.cot:
                u = parent.children
                u_prime = derive_operation(u, with_respect_to=with_respect_to)
                two = node(operations.const, 2)
                minus_one = node(operations.const, -1)
                return minus_one*(csc(u)**two)*u_prime
            
            case operations.asin:
                u = parent.children
                u_prime = derive_operation(u, with_respect_to=with_respect_to)
                one = node(operations.const, 1)
                half = node(operations.const, 0.5)
                return (one / ((one-(u*u))**half))*u_prime

            case operations.acos:
                negative_one = node(operations.const, -1)
                u = parent.children
                u_prime = derive_operation(u, with_respect_to=with_respect_to)
                one = node(operations.const, 1)
                half = node(operations.const, 0.5)
                return negative_one * (one / ((one-(u*u))**half))*u_prime

            case operations.atan:
                u = parent.children
                u_prime = derive_operation(u, with_respect_to=with_respect_to)
                one = node(operations.const, 1)
                return one / (one + u*u) * u_prime

            case operations.asec:
                u = parent.children
                u_prime = derive_operation(u, with_respect_to=with_respect_to)
                one = node(operations.const, 1)
                half = node(operations.const, 0.5)
                return abs(one / (u * (u*u - 1)**half) * u_prime)
            
            case operations.acsc:
                negative_one = node(operations.const, -1)
                u = parent.children
                u_prime = derive_operation(u, with_respect_to=with_respect_to)
                one = node(operations.const, 1)
                half = node(operations.const, 0.5)
                return negative_one * abs(one / (u * (u*u - 1)**half) * u_prime)
            
            case operations.acot:
                negative_one = node(operations.const, -1)
                u = parent.children
                u_prime = derive_operation(u, with_respect_to=with_respect_to)
                one = node(operations.const, 1)
                return negative_one * one / (one + u*u) * u_prime

        raise ValueError(f"non-differentiable operation detected: {reverser[parent.arg]}")
    elif (parent.op == operations.const) or (parent.op == operations.void):
        a = node(operations.void, None)
        return a
    elif parent.op == operations.var:
        if with_respect_to == "all":
            var_prime = node(operations.var, f"{parent.arg}'")

            var_var_prime = node(operations.operation, operations.mult,
            children=(parent, var_prime))

            return var_prime
        else:
            if with_respect_to == parent.arg:
                var_prime = node(operations.var, f"{parent.arg}'")

                var_var_prime = node(operations.operation, operations.mult,
                children=(parent, var_prime))

                return var_prime
            else:
                return node(operations.void, None)

    else:
        pass