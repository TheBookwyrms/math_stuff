import collections


class operations:
    void = -7

    const = 0
    var = 1

    add = 8
    sub = 9
    mult = 10
    div = 11

    pow = 14
    ln = 15

    sin = 21
    cos = 22
    tan = 23
    sec = 24
    csc = 25
    cot = 26

    asin = 31
    acos = 32
    atan = 33
    asec = 34
    acsc = 35
    acot = 36

    floor = 41
    ceil = 42

    abs = 45


class node:
    def __init__(
        self,
        type_: str, # "operation_type", "const", or "var", or "void"
        details: str, # argument of type
        children = [], # always pass tuple when making a node
    ):
        self.op = type_
        self.arg = details
        self.children = children
        self.has_var = True

        if self.length(self) == 0:
            self.is_differentiable = True
            if self.op == "const":
                self.has_var = False
        elif self.length(self) == -1:
            self.is_differentiable = self.children.is_differentiable
            if (self.children.op != "var"):
                self.has_var = False
        elif self.length(self) == 2:
            try:
                if (self.children[0].op != ("const" or "var")) and (self.children[1].op != ("const" or "var")):
                    self.is_differentiable = self.children[0].is_differentiable and self.children[1].is_differentiable
                if (self.children[0].op == ("const" or "var")) and (self.children[1].op != ("const" or "var")):
                    self.is_differentiable = self.children[1].is_differentiable
                if (self.children[0].op != ("const" or "var")) and (self.children[1].op == ("const" or "var")):
                    self.is_differentiable = self.children[0].is_differentiable
                if (self.children[0].op == ("const" or "var")) and (self.children[1].op == ("const" or "var")):
                    self.is_differentiable = True
                if (self.op == 10) or (self.op == 11):
                    a = self.children[0].has_var
                    b = self.children[1].has_var
                    c = a or b
                    self.has_var = c
                    if (self.has_var) and ((self.op == "operation_type") and (self.arg == (('operation_type', 10) or ('operation_type', 11)))):
                        self.children[0].has_var = True
                        self.children[1].has_var = True
            except:
                self.is_differentiable = True
            else:
                self.has_var = False

    def __len__(self):
        x = 0
        #if self.children != []:
        try:
            for child in self.children:
                x += 1
        except:
            x = -1
        return x
    
    def length(self, parent):
        x = 0
        try:
            x = len(parent)
        except:
            x = -1
        return x


    def __add__(self, sibling):
        new_parent = node("operation_type", operations.add, children=(self, sibling))

        return new_parent

    def __sub__(self, sibling):
        new_parent = node("operation_type", operations.sub
        , children=(self, sibling))

        return new_parent

    def __mul__(self, sibling):
        new_parent = node("operation_type", operations.mult
        , children=(self, sibling))

        return new_parent

    def __truediv__(self, sibling):
        new_parent = node("operation_type", operations.div
        , children=(self, sibling))

        return new_parent

    def __pow__(self, sibling):
        new_parent = node("operation_type", operations.pow
        , children=(self, sibling))

        return new_parent

    def __abs__(self):
        new_parent = node("operation_type", operations.abs
        , children=(self))

        self.is_differentiable = False

        return new_parent

def ln(self):
    new_parent = node("operation_type", operations.ln
    , children=(self))

    return new_parent

def sin(self):
    new_parent = node("operation_type", operations.sin
    , children=(self))

    return new_parent

def cos(self):
    new_parent = node("operation_type", operations.cos
    , children=(self))

    return new_parent

def tan(self):
    new_parent = node("operation_type", operations.tan
    , children=(self))

    return new_parent

def sec(self):
    new_parent = node("operation_type", operations.sec
    , children=(self))

    return new_parent

def csc(self):
    new_parent = node("operation_type", operations.csc
    , children=(self))

    return new_parent

def cot(self):
    new_parent = node("operation_type", operations.cot
    , children=(self))

    return new_parent

def asin(self):
    new_parent = node("operation_type", operations.asin
    , children=(self))

    return new_parent

def acos(self):
    new_parent = node("operation_type", operations.acos
    , children=(self))

    return new_parent

def atan(self):
    new_parent = node("operation_type", operations.atan
    , children=(self))

    return new_parent

def asec(self):
    new_parent = node("operation_type", operations.asec
    , children=(self))

    return new_parent

def acsc(self):
    new_parent = node("operation_type", operations.acsc
    , children=(self))

    return new_parent

def acot(self):
    new_parent = node("operation_type", operations.acot
    , children=(self))

    return new_parent

def floor(self):
    new_parent = node("operation_type", operations.floor
    , children=(self))

    self.is_differentiable = False

    return new_parent

def ceil(self):
    new_parent = node("operation_type", operations.ceil
    , children=(self))

    self.is_differentiable = False

    return new_parent