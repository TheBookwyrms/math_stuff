from tree_builder_1 import *

print(eval("sin(3)"))

a = node(operations.const, {"const", 5})
b = node(operations.const, {"const", -7})
res1 = (sin(ln(acos(a+b)))/(atan(b**(a**(b*abs(ln(a)))))))-b
res2 = a*b-a
print()

reverser = {
    0: "const",
    1: "var",
    8: "+",
    9: "-",
    10: "*",
    11: "/"}

new = collections.deque(range(0))
args = dict
current_op = res2
done = False

if type(current_op.args) == dict:
    new.append(reverser[current_op.args['operation_type']])
    for child in current_op.children:
        if type(child.args) == dict:
            for child2 in child.children:
                if type(child2.args) != dict:
                    new.append(child2.args)
                else:
                    new.append(reverser[child2.args['operation_type']])
            new.append(reverser[child.args['operation_type']])
        else:
            new.append(child.args)
else:
    new.append(current_op.args)

print(new)





c = res2.args['operation_type']
new.append(reverser[c])
print(new)

for child in res2.children:
    print(child.args)

t = collections.deque(range(5))
#t.appendleft(18)
#t.insert(2, 80)
print(t)