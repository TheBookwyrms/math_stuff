from tree_builder_2 import *
from tree_decoder_test_2 import *
from derive_operation import *

aao = node("const", 1)
aat = node("const", 2)
aath = node("const", 3)
aaf = node("const", 4)
aafi = node("const", 5)
aa_s = node("const", -7)
aax = node("var", "x")


ch = (aaf*(aax**aat))/(aath*(aax**aath))
t = derive_operation(ch)

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
#print(call_maker(p))