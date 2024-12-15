class Operations:
    CONST = 0
    VARIABLE = 1

    BASIC = 4
    TRIG = 8

class OperationImpl:
    def __init__(self):
        ...

    def _get_type(self):
        raise NotImplementedError()

    def operate(self, op_args: dict):
        self._operate(*op_args)

    def _operate(self, *args, **kwargs):
        raise NotImplementedError("Operation needs to implement")

class Const(OperationImpl):
    def _get_type(self):
        return Operations.CONST
    
    def _operate(self, const):
        return const


# class Variable(OperationImpl):
#     def _get_type(self):
#         return Operations.VARIABLE
    
#     def _operate(self, variable_name):
#         return variable_name


class Basic(OperationImpl):
    ADD = 0
    SUB = 1

    def _get_type(self):
        return Operations.BASIC
    
    def _operate(self, operation_type):
        return operation_type



class Node:
    def __init__(
        self,
        op: Operations,
        op_args: dict, 
        children=(),
    ):
        if op == Operations.CONST:
            self.op = Const()
        # elif op == Operations.VARIABLE:
        #     self.op = Variable()
        elif op == Operations.BASIC:
            self.op = Basic()

        self.op_args = op_args
        self.children = children

    def __add__(self, sibling_node):
        new_parent = Node(Operations.BASIC, op_args={
            "operation_type": Basic.ADD
        }, children=(self, sibling_node))

        return new_parent

    def __sub__(self, sibling_node):
        new_parent = Node(Operations.BASIC, op_args={
            "operation_type": Basic.SUB
        }, children=(self, sibling_node))

        return new_parent


a = Node(Operations.CONST, {"const", 5})
b = Node(Operations.CONST, {"const", 7})

res = a - b
print(res)

# def sin(tree: Node):
#     ...

# def cos(tree: Node):
#     ...


# def parse_nodes(string):