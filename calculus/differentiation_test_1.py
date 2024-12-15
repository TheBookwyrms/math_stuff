from tree_builder import *
from tree_decoder_test_3 import *

a = node(operations.const, ("const", 5))
b = node(operations.const, ("const", -7))
b = node(operations.var, ("var", "x"))

p = a/b+sin(a+a)
#p = a/b+sin(a+a)

print()
print(call_maker(p))

reverser = {
    8: "+",
    9: "-",
    10: "*",
    11: "/",
    14: "**",
    15: "ln",
    21: "sin",
    22: "cos",
    23: "tan",
    24: "sec",
    25: "csc",
    26: "cot",
    31: "asin",
    32: "acos",
    33: "atan",
    34: "asec",
    35: "acsc",
    36: "atan",
    41: "floor",
    42: "ceil",
    45: "abs"}


x = 0

def perform_differentiation(path, equation, can_differentiate, parent: node):
    global x
    x += 1

    if parent.is_differentiable == False:
        can_differentiate = False

    #print(parent.args, parent.has_var)

    if parent not in path:
        if (parent.args[0] == "const") or (parent.args[0] == "var"):
            #print(parent.args, parent.has_var, 1.1, x)
            # case when parent is "const" or "var"
            equation.append(parent.args[1])
            path.append(parent)

        elif parent.length(parent) == -1:
            #print(parent.args, parent.has_var, 1.2, x)
            #print(parent.args, parent.children.args, parent.has_var, parent.children.has_var)
            if (parent.children.args[0] == "const"):
                equation.append(parent.children.args[1])
                parent.args = ("const", parent.children.args[1])
                #parent.args = parent.children.args 
            else:
                equation.append(reverser[parent.args[1]])
                equation.append("(")
                path, equation, can_differentiate = perform_differentiation(path, equation, can_differentiate, parent.children)
                equation.append(")")
                #if parent.has_var:
                #    print(parent.has_var)
                #print(parent.args, parent.children.args, not parent.has_var, "aaaaa")
            
            #print(parent.has_var)
            if (parent.children.args[0] == "const") and (not parent.has_var):
                #print(parent.args, parent.children.args, "atest")
                equation.pop()
                equation.pop()
                equation.pop()
                equation.pop()
                equation.append(0)
            path.append(parent)
        elif len(parent) == 2:
            # case where this is on operation containing two sub-nodes
            if (parent.children[0].args[0] == "const") and (parent.children[1].args[0] == "const"):
                #print(parent.args, parent.has_var, "1.3.1", x)
                full = str(parent.children[0].args[1])+str(reverser[parent.args[1]])+str(parent.children[0].args[1])
                equation.append(full)
                parent.args = ("const", full)

            else:
                #if (parent.args[1] == 10 or parent.args[1] == 11) and (parent.has_var):
                #    print(parent.args, "1.3.2.1", x)
                #    pass
                #else:
                    #print(parent.args, parent.has_var, "1.3.2", x)
                    equation.append("(")
                    path, equation, can_differentiate = perform_differentiation(path, equation, can_differentiate, parent.children[0])
                    equation.append(reverser[parent.args[1]])
                    path.append(parent)
                    path, equation, can_differentiate = perform_differentiation(path, equation, can_differentiate, parent)
                    equation.append(")")
                
            #print(parent.has_var)
            if (parent.children[0].args[0] == "const") and (parent.children[1].args[0] == "const") and (parent.has_var):
                #print(parent.args, parent.children[0].args, parent.children[1].args, "atest")
                equation.pop()
                equation.pop()
                equation.pop()
                equation.pop()
            pass
        else:
            #print(parent.args, 1.4, x)
            pass

    elif parent in path:
        if (parent.args[0] == "const") or (parent.args[0] == "var"):
            #print(parent.args, parent.has_var, 2.1, x)
            # case when parent is "const" or "var"
            equation.append(parent.args[1])
        elif parent.length(parent) == -1:
            #print(parent.args, parent.has_var, 2.2, x)
            pass # intentional
        elif len(parent) == 2:
            # case where this is on operation containing two sub-nodes
            if (parent.children[0].args[0] == "const") and (parent.children[1].args[0] == "const"):
                #print(parent.args, parent.has_var, "2.3.1", x)
                full = str(parent.children[0].args[1])+str(reverser[parent.args[1]])+str(parent.children[0].args[1])
                equation.append(full)
                parent.args = ("const", full)
            else:
                #print(parent.args, parent.has_var, "2.3.2", x)
                #print("1", parent.has_var, parent.children[0].has_var, parent.children[1].has_var)
                #print(parent.children[0].args, parent.children[1].args)
                a = parent.children[0].has_var
                b = parent.children[1].has_var
                c = a or b
                parent.has_var = c
                #print("1", parent.has_var, parent.children[0].has_var, parent.children[1].has_var)
                if (parent.has_var) and (parent.args == (('operation_type', 10) or ('operation_type', 11))):
                    parent.children[0].has_var = True
                    parent.children[1].has_var = True
                #print("2", parent.has_var, parent.children[0].has_var, parent.children[1].has_var)

                #print(f"     ...     a: {a}, b: {b}, c: {c}     ...")
                #print("test", parent.args, parent.has_var, "test")
                path, equation, can_differentiate = perform_differentiation(path, equation, can_differentiate, parent.children[1])

            #print("test", parent.args, parent.has_var, "test")


        else:
            #print(parent.args, 2.4, parent.has_var, x)
            pass
        

    else:
        #print(parent.args, parent.has_var, 3, x)
        pass

    return path, equation, can_differentiate



def differentiate(tree):
    path = collections.deque(range(1))
    equation = collections.deque(range(0))
    can_differentiate = True
    path, equation, can_differentiate = perform_differentiation(path, equation, can_differentiate, tree)
    as_one = "".join([str(i) for i in equation])

    if can_differentiate == False:
        raise ValueError("cannot be differentiated")

    return as_one


print(differentiate(p))

print()