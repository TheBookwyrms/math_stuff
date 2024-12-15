from tree_builder import *

a = node(operations.const, ("const", 5))
b = node(operations.const, ("const", -7))

p = sin(a+a)*b


print()

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
    45: "abs"}

path = collections.deque(range(1))
equation = collections.deque(range(0))

def maker(path, equation, parent: node):
    if parent not in path:
        if (parent.children == []):
            # case when parent is "const" or "var"
            equation.append(parent.args[1])
            path.append(parent)
            #path, equation = maker(path, equation, parent)
        #     pass
        elif parent.length(parent) == -1:
            equation.append(reverser[parent.args[1]])
            equation.append("(")
            path, equation = maker(path, equation, parent.children)
            equation.append(")")
            path.append(parent)
        elif len(parent) == 2:
            # case where this is on operation containing two sub-nodes
            path, equation = maker(path, equation, parent.children[0])
            equation.append(reverser[parent.args[1]])
            #equation.append(parent.children[0].args[1])
            path.append(parent)
            path, equation = maker(path, equation, parent)
            pass
    elif parent in path:
        if (parent.children == []):
            # case when parent is "const" or "var"
            equation.append(parent.args[1])
            path.append(parent)
            #path, equation = maker(path, equation, parent)
        elif parent.length(parent) == -1:
            pass
        elif len(parent) == 2:
            # case where this is on operation containing two sub-nodes
            path, equation = maker(path, equation, parent.children[1])
    
    return path, equation


path, equation = maker(path, equation, p)
print(equation)
as_one = "".join([str(i) for i in equation])
print(as_one)

print()







def test():
    parent = sin(a)

    path = collections.deque(range(1))
    equation = collections.deque(range(0))

    def getter(path, equation, parent):
        if type(parent.args) == dict:
            if parent == path[-1]:
                pass
            else:
                print(len(parent.children))
        else:
            equation.append(parent.args[1])
        
        return path, equation, parent

    path, equation, parent = getter(path, equation, parent)