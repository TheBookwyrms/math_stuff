class operations:
    def __init__(self):
        self.sin = 0
        self.cos = 1

    
    def testing(self):
        return 5

class nodes(operations):
    def __init__(self, string):
        operations.__init__(self)

        class children_type:
            def __init__(self, thing):
                self.tree = []
                self.thing = thing
            def returner(self):
                return self.thing

        tree = children_type.__init__(self, "")

        def sin(u):
            sin = children_type("sin")
            sin = sin.returner()
            u = children_type(u)
            self.tree.append(u)
            return [sin, u]
        
        def cos(u):
            cos = children_type("cos")
            cos = cos.returner()
            u = children_type(u)
            return [cos, u]
        
        def __add__(self, other):
            return [self, other]
        
        b = eval(string)
        print(b)
        print(self.tree)
        for i in b:
            print(str(i))

f = nodes("cos(sin(cos(2)))")


# class parser:
#     def __init__(self):
#         self.sin = 0
#         self.cos = 1
#         def __add__(self, other):
#             print("worked")
#             return [self.sin].append(other)
        
#         def sin(u):
#             test = (self.sin)+(u)
#             return test
        
#         self.d = eval("sin(3)")


# #a = nodes("sin(3)")
# #print(a.testing())
# print()
# c = parser()
# print(c.d)