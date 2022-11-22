import random
from utils import Expression

def get_tests():
    tests = []
    n = 50
    symbols = list(map(Expression, list(map(chr, range(65, 91))) + [a+a for a in list(map(chr, range(65, 89)))] ))
    print('symbols:', symbols)
    ratios = [i * 0.5 for i in range(2, 12)]
    m_list = [int(r * n) for r in ratios]
    for j, m in enumerate(m_list):
        print('m:', m)
        test = []
        clauses = []
        for c in range(m):
            literals = []
            possible_symbols = symbols.copy()
            for i in range(3):
                symbol = random.choice(possible_symbols)
                literal = symbol if random.choice([True, False]) else ~symbol
                literals.append(literal)
                possible_symbols.remove(symbol)
            
            clause = (literals[0] | literals[1] | literals[2])
            clauses.append(clause)
            # print(literals, clause)
        test = clauses
        tests.append(test)
        print(f'test{j+1}:', test)
    return tests


        
            
            

    