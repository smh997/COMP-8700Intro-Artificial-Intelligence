import random
from utils import *

def waliksat(clauses, p, max_flips):
    symbols = set() # Set of symbols in clauses
    for clause in clauses:
        for symbol in clause_symbols(clause):
            symbols.add(symbol)

    model = dict() # model <- a random assignment of true/false to the symbols in clauses
    for symbol in symbols:
        model[symbol] = random.choice([True, False])
    
    for i in range(max_flips):
        unsatisfied_clauses = []
        for clause in clauses:
            if not pl_true(clause, model):
                unsatisfied_clauses.append(clause)
        if len(unsatisfied_clauses) == 0:  
            return model # model satisfies all the clauses

        clause = random.choice(unsatisfied_clauses) # a randomly selected clause from unsatisfied clauses (clauses that are false in model)
        
        if random.uniform(0.0, 1.0) <= p:
            symbol = random.choice(list(clause_symbols(clause))) # flip the value in model of a randomly selected symbol from clause
        else:
            # Flip whichever symbol in clause maximizes the number of satisfied clauses
            def count_satisfied_clauses(symbol):
                model[symbol] = not model[symbol]
                list_of_satisfied_clauses = []
                for clause in clauses:
                    if pl_true(clause, model):
                        list_of_satisfied_clauses.append(clause)
                c = len(list_of_satisfied_clauses)
                model[symbol] = not model[symbol]
                return c

            symbol = max(clause_symbols(clause), key=count_satisfied_clauses)
        model[symbol] = not model[symbol]

    return None # failure