from tree_builder_1 import *

a = node(operations.const, ("const", 5))
#b = node(operations.const, ("const", -7))
b = node(operations.var, ("var", "x"))

p = a/b+sin(a+a)*b
p = a**b*sin(b**a)
p = a**b
print(p.args)
print(p.children[0].args)
print(p.children[1].args)

#print()

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


def maker(path, equation, parent: node):
    if parent not in path:
        if (parent.children == []):
            # case when parent is "const" or "var"
            equation.append(parent.args[1])
            path.append(parent)
        elif parent.length(parent) == -1:
            equation.append(reverser[parent.args[1]])
            equation.append("(")
            path, equation = maker(path, equation, parent.children)
            equation.append(")")
            path.append(parent)
        elif len(parent) == 2:
            # case where this is on operation containing two sub-nodes
            equation.append("(")
            path, equation = maker(path, equation, parent.children[0])
            equation.append(reverser[parent.args[1]])
            path.append(parent)
            path, equation = maker(path, equation, parent)
            equation.append(")")
            pass
    elif parent in path:
        if (parent.children == []):
            # case when parent is "const" or "var"
            equation.append(parent.args[1])
            path.append(parent)
        elif parent.length(parent) == -1:
            pass # intentional
        elif len(parent) == 2:
            # case where this is on operation containing two sub-nodes
            path, equation = maker(path, equation, parent.children[1])
    
    return path, equation



def call_maker(tree):
    path = collections.deque(range(1))
    equation = collections.deque(range(0))
    path, equation = maker(path, equation, tree)
    as_one = "".join([str(i) for i in equation])

    return as_one


print(call_maker(p))

#print()