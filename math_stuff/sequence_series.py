from math_stuff.node_class import *

class SequencenException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class Sequence:
    def __init__(self, general_term:Node, var_of_sequence_iteration:str):
        self.general_term = general_term
        self.n = var_of_sequence_iteration

    def get_n_terms(self, last_term:int=10, first_term:int=0, step:int=1, specific_terms=None):
        iteration_terms = [first_term, last_term, step]
        all_terms_int = all([True if type(term)==int else False for term in iteration_terms])
        if not all_terms_int:
            raise SequencenException('first term, last term, and step must be integers')
        terms = []
        if specific_terms == None:
            for i in range(*iteration_terms):
                terms.append(self.general_term.sub_variables({self.n:i}))            
        else:
            for i in specific_terms:
                if type(i) != int:
                    raise Sequence('nth term must be an integer')
                terms.append(self.general_term.sub_variables({self.n:i}))            

        return tuple(terms)

def run_3():

    n = Node(subtypes.VAR, "n")
    b = Node(subtypes.VAR, "b")
    two = Node(subtypes.NUMBER, 2)
    an = tan(two*n*b)
    sq = Sequence(an, n.value)
    terms = sq.get_n_terms(5)
    print(tuple([str(t) for t in terms]))