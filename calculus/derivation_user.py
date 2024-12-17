from tree_builder_2 import *
from tree_decoder_test_2 import *
from derive_operation import *

a = node(operations.const, ("const", 5))
b = node(operations.const, ("const", -7))
b = node(operations.var, ("var", "x"))

p = a/b+sin(a+(a/(a*b)))
p = ln(a)
p = sin(a+b)
#p = a/b+sin(a+a)




t = derive_operation(((a*b)*(b**a))**a)

print()
print(call_maker(t), "test")
print()

# def derive(to_pass, parent):
#     if can_differentiate == False:
#         raise ValueError("cannot be differentiated")
    

#     path, equation, can_differentiate = to_pass
#     if parent not in path:
#         pass

#     elif parent in path:
#         pass

#     else:
#         raise ValueError("parent neither in nor not in path")
    

def derive(tree):
    #to_pass = [collections.deque(range(1)), # path
    #           collections.deque([0, 0, "+"]), # equation
    #           True] # can_differentiate
    #path, equation, can_differentiate = derive(to_pass, tree)
    #as_one = "".join([str(i) for i in equation])

    #if can_differentiate == False:
    #    raise ValueError("cannot be differentiated")

    #return as_one
    pass
print(call_maker(p))