from tree_builder import *

a = node(operations.const, {"const", 5})
b = node(operations.const, {"const", -7})

parent = a+b

for child in parent.children:
    print(child.args)

path = collections.deque(range(0))
final = collections.deque(range(0))

def getter(path, final, parent):
    
    while (type(parent.args) == dict) and (parent not in path):
        path.append(parent)
        print(path)
        try:
            for child in parent.children:
                final.append(getter(path, final, child))
        except:
            child = path[-1]
            path.pop(-1)


    return path, final

path, final = getter(path, final, parent)
print()
print(path)
print(final)
print()

b = sin(a)
c = b.children
print()