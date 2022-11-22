from walksat import *
from three_CNF_generator import get_tests


def test():
    def check(clauses):
        solution = waliksat(clauses, p=0.5, max_flips=10000)
        if solution:
            return solution, all(pl_true(clause, solution) for clause in clauses)
        else:
            return 'Failure'      

    for j, test in enumerate(get_tests()):
        print(f'test {j+1}:', check(test))
        print()

test()