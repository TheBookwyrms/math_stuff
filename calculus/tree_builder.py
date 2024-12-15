import collections


class operations:
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
        type_: operations,
        details, # always pass tuple when making a node
        children = [], # always pass tuple when making a node
    ):
        self.op = type_
        self.args = details
        self.children = children

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
        new_parent = node(operations.add, details=
            ("operation_type", operations.add), children=(self, sibling))

        return new_parent

    def __sub__(self, sibling):
        new_parent = node(operations.sub, details=
            ("operation_type", operations.sub)
        , children=(self, sibling))

        return new_parent

    def __mul__(self, sibling):
        new_parent = node(operations.mult, details=
            ("operation_type", operations.mult)
        , children=(self, sibling))

        return new_parent

    def __truediv__(self, sibling):
        new_parent = node(operations.div, details=
            ("operation_type", operations.div)
        , children=(self, sibling))

        return new_parent

    def __pow__(self, sibling):
        new_parent = node(operations.pow, details=
            ("operation_type", operations.pow)
        , children=(self, sibling))

        return new_parent

    def __abs__(self):
        new_parent = node(operations.abs, details=
            ("operation_type", operations.abs)
        , children=(self))

        return new_parent

def ln(self):
    new_parent = node(operations.ln, details=
        ("operation_type", operations.ln)
    , children=(self))

    return new_parent

def sin(self):
    new_parent = node(operations.sin, details=
        ("operation_type", operations.sin)
    , children=(self))

    return new_parent

def cos(self):
    new_parent = node(operations.cos, details=
        ("operation_type", operations.cos)
    , children=(self))

    return new_parent

def tan(self):
    new_parent = node(operations.tan, details=
        ("operation_type", operations.tan)
    , children=(self))

    return new_parent

def sec(self):
    new_parent = node(operations.sec, details=
        ("operation_type", operations.sec)
    , children=(self))

    return new_parent

def csc(self):
    new_parent = node(operations.csc, details=
        ("operation_type", operations.csc)
    , children=(self))

    return new_parent

def cot(self):
    new_parent = node(operations.cot, details=
        ("operation_type", operations.cot)
    , children=(self))

    return new_parent

def asin(self):
    new_parent = node(operations.asin, details=
        ("operation_type", operations.asin)
    , children=(self))

    return new_parent

def acos(self):
    new_parent = node(operations.acos, details=
        ("operation_type", operations.acos)
    , children=(self))

    return new_parent

def atan(self):
    new_parent = node(operations.atan, details=
        ("operation_type", operations.atan)
    , children=(self))

    return new_parent

def asec(self):
    new_parent = node(operations.asec, details=
        ("operation_type", operations.asec)
    , children=(self))

    return new_parent

def acsc(self):
    new_parent = node(operations.acsc, details=
        ("operation_type", operations.acsc)
    , children=(self))

    return new_parent

def acot(self):
    new_parent = node(operations.acot, details=
        ("operation_type", operations.acot)
    , children=(self))

    return new_parent

def floor(self):
    new_parent = node(operations.floor, details=
        ("operation_type", operations.floor)
    , children=(self))

    return new_parent

def ceil(self):
    new_parent = node(operations.ceil, details=
        ("operation_type", operations.ceil)
    , children=(self))

    return new_parent