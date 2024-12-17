from tree_builder_2 import *
from tree_decoder_test_2 import *


def derive_operation(self):
    if self.args[0] == "operation_type":
        match self.args[1]:
            case 8:
                return self
            case 9:
                return self
            case 10:
                a = self.children[0]
                b = self.children[1]
                aa = derive_operation(a)
                bb = derive_operation(b)
                #aa.is_differentiable = True
                #bb.is_differentiable = True

                new_child_1 = node(operations.mult, details=
                ("operation_type", operations.mult),
                children=(aa, b))

                new_child_2 = node(operations.mult, details=
                ("operation_type", operations.mult),
                children=(a, bb))

                new_parent = node(operations.add, details=
                ("operation_type", operations.add),
                children=(new_child_1, new_child_2))



                return new_parent
            case 11:
                new_parent = node(operations.div, details=
                    ("operation_type", operations.div)
                , children=(self))

                self.is_differentiable = True

                return new_parent
            case 14:
                if self.children[1].args[0] == "const":
                    one = node(operations.const, ("const", 1))
                    u = self.children[0]
                    to_the_n = self.children[1]

                    new_base_power = node(operations.pow, details=
                    ("operation_type", operations.pow)
                    , children=(u, to_the_n-one))

                    front__power = node(operations.mult, details=
                    ("operation_type", operations.mult)
                    , children=(to_the_n, new_base_power))

                    u_prime = derive_operation(u)

                    with_u_prime = node(operations.mult, details=
                    ("operation_type", operations.mult)
                    , children=(front__power, u_prime))

                    return with_u_prime
                else:
                    pass # TODO logarithmic differentiation
                    raise ValueError("logarithmic differentiation not implemented yet")
            case 15:
                pass
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
    elif self.args[0] == "const":
        a = node(operations.void, ("void", None))
        return a
    elif self.args[0] == "var":
        var_prime = node(operations.var, ("var", f"{self.args[1]}'"))

        var_var_prime = node(operations.mult, details=
        ("operation_type", operations.mult),
        children=(self, var_prime))

        return var_prime
    else:
        pass