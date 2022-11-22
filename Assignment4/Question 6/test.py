from walksat import *

A, B, C, D, E, F, G, P, Q, a, x, y, z, u = map(Expr, 'ABCDEFGPQaxyzu')

def test_WalkSAT():
    def check_SAT(clauses):
        # Make sure the solution is correct if it is returned by WalkSat
        # Sometimes WalkSat may run out of flips before finding a solution
        sol = WalkSAT(clauses)
        if sol:
            return sol, all(pl_true(x, sol) for x in clauses)          

    # Test WalkSat for problems with solution
    print(check_SAT([A & B, A & C]))
    print(check_SAT([A | B, P & Q, P & B]))
    print(check_SAT([A & B, C | D, ~(D | P)]))
    print(check_SAT([A, B, ~C, D]))
    print()

    # print(check_SAT([]))

    print()
    # Test WalkSat for problems without solution
    print(WalkSAT([A & ~A], 0.5))
    print(WalkSAT([A & B, C | D, ~(D | B)], 0.5))
    print(WalkSAT([A | B, ~A, (B | C), C | D, P | Q], 0.5, 10))
    print(WalkSAT([A | B, B & C, C | D, D & A, P, ~P], 0.5))


test_WalkSAT()