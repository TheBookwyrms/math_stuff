import collections

def colourer(colour_code):
    return f'\033[{colour_code}m'

reverser = {
        -100: "operation",
        -7: "void",
        0: "const",
        1: "var",
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
        36: "cot",
        41: "floor",
        42: "ceil",
        45: "abs"}

class operations:
    operation = -100
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
        type_: str, # operations.operation, operations.const, or operations.var, or operations.void
        details: str, # argument of type
        children = [], # always pass tuple when making a node
    ):
        self.op = type_
        self.arg = details
        self.children = children
        
   
    def length(self):
        x = 0
        try:
            for child in self.children:
                x += 1
        except:
            x = 0
            if self.op == operations.operation:
                x=1
        return x
    

    def __str__(self):
        match self.length():
            case 0:
                if (self.op == operations.const) or (self.op == operations.var):
                    return f'{self.arg}'
                elif self.op == operations.void:
                    return "None"
                elif self.op == operations.operation:
                    return f'{reverser[self.arg]}({self.children})'
                else:
                    raise ValueError("3thrd case case 0", self.op, self.arg)
            case 1:
                return f'{reverser[self.arg]}({str(self.children)})'
            case 2:
                return f'({str(self.children[0])}{reverser[self.arg]}{str(self.children[1])})'
        #print(self.length())
        raise ValueError("error in case", self.length())


    def __add__(self, sibling):
        new_parent = node(operations.operation, operations.add, children=(self, sibling))

        return new_parent

    def __sub__(self, sibling):
        new_parent = node(operations.operation, operations.sub
        , children=(self, sibling))

        return new_parent

    def __mul__(self, sibling):
        new_parent = node(operations.operation, operations.mult
        , children=(self, sibling))

        return new_parent

    def __truediv__(self, sibling):
        new_parent = node(operations.operation, operations.div
        , children=(self, sibling))

        return new_parent

    def __pow__(self, sibling):
        new_parent = node(operations.operation, operations.pow
        , children=(self, sibling))

        return new_parent
    
    

def abs(self):
    new_parent = node(operations.operation, operations.abs
    , children=(self))

    self.is_differentiable = False

    return new_parent

def ln(self):
    new_parent = node(operations.operation, operations.ln
    , children=(self))

    return new_parent

def sin(self):
    new_parent = node(operations.operation, operations.sin
    , children=(self))

    return new_parent

def cos(self):
    new_parent = node(operations.operation, operations.cos
    , children=(self))

    return new_parent

def tan(self):
    new_parent = node(operations.operation, operations.tan
    , children=(self))

    return new_parent

def sec(self):
    new_parent = node(operations.operation, operations.sec
    , children=(self))

    return new_parent

def csc(self):
    new_parent = node(operations.operation, operations.csc
    , children=(self))

    return new_parent

def cot(self):
    new_parent = node(operations.operation, operations.cot
    , children=(self))

    return new_parent

def asin(self):
    new_parent = node(operations.operation, operations.asin
    , children=(self))

    return new_parent

def acos(self):
    new_parent = node(operations.operation, operations.acos
    , children=(self))

    return new_parent

def atan(self):
    new_parent = node(operations.operation, operations.atan
    , children=(self))

    return new_parent

def asec(self):
    new_parent = node(operations.operation, operations.asec
    , children=(self))

    return new_parent

def acsc(self):
    new_parent = node(operations.operation, operations.acsc
    , children=(self))

    return new_parent

def acot(self):
    new_parent = node(operations.operation, operations.acot
    , children=(self))

    return new_parent

def floor(self):
    new_parent = node(operations.operation, operations.floor
    , children=(self))

    self.is_differentiable = False

    return new_parent

def ceil(self):
    new_parent = node(operations.operation, operations.ceil
    , children=(self))

    self.is_differentiable = False

    return new_parent