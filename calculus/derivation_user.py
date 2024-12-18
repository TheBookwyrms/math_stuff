from tree_builder_2 import *
from derive_operation import *

aao = node("const", 1)
aat = node("const", 2)
aath = node("const", 3)
aaf = node("const", 4)
aafi = node("const", 5)
aa_s = node("const", -7)
aax = node("var", "x")

ch = aao/(aath*(aax**aath))
ch = (aath*(aax**aat))/(aax*aax*aax*aat)
#ch = (aax*aax*aax*aat)
#ch = ch+aafi
t = derive_operation(ch)
print()
print(ch)
print()
print(t)

print()