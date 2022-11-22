from math import log, ceil
class State:

    def __init__(self, name, passed_actions=[]):
        self.name = name
        self.passed_actions = passed_actions
        self.ply = len(self.passed_actions)

class Game:
    def __init__(self, ply, root_state, four_ply_index=0):
        self.ply = ply
        self.four_ply_index = four_ply_index
        self.states = [root_state]
        self.possible_actions = []
        if self.ply == 2:
            self.possible_actions = {'A': ['a1', 'a2', 'a3'],
                                     'B': ['b1', 'b2', 'b3'], 'C': ['c1', 'c2', 'c3'], 'D': ['d1', 'd2', 'd3']}
            self.result_of = {'a1': 'B', 'a2': 'C', 'a3': 'D', 
                              'b1': 'E', 'b2': 'F', 'b3': 'G', 
                              'c1': 'H', 'c2': 'I', 'c3': 'J', 
                              'd1': 'K', 'd2': 'L', 'd3': 'M'}
            self.utility_values = {'E': 3, 'F': 12, 'G': 8,
                                   'H': 2, 'I': 4, 'J': 6,
                                   'K': 14, 'L': 5, 'M': 2}
            # self.utility_values = {('a1', 'b1'): 3, ('a1', 'b2'): 12, ('a1', 'b3'): 8,
            #                        ('a2', 'c1'): 2, ('a2', 'c2'): 4, ('a2', 'c3'): 6,
            #                        ('a3', 'd1'): 14, ('a3', 'd2'): 5, ('a3', 'd3'): 2}
        else:
            self.possible_actions = {'A': ['a1', 'a2'],
                                     'B': ['b1', 'b2'], 'C': ['c1', 'c2'], 
                                     'D': ['d1', 'd2'], 'E': ['e1', 'e2'], 'F': ['f1', 'f2'], 'G': ['g1', 'g2'],
                                     'H': ['h1', 'h2'], 'I': ['i1', 'i2'], 'J': ['j1', 'j2'], 'K': ['k1', 'k2'], 'L': ['l1', 'l2'], 'M': ['m1', 'm2'], 'N': ['n1', 'n2'], 'O': ['o1', 'o2']}
            self.result_of = {'a1': 'B', 'a2': 'C', 
                              'b1': 'D', 'b2': 'E', 
                              'c1': 'F', 'c2': 'G', 
                              'd1': 'H', 'd2': 'I',
                              'e1': 'J', 'e2': 'K',
                              'f1': 'L', 'f2': 'M',
                              'g1': 'N', 'g2': 'O',
                              'h1': 'P', 'h2': 'Q',
                              'i1': 'R', 'i2': 'S',
                              'j1': 'T', 'j2': 'U',
                              'k1': 'V', 'k2': 'W',
                              'l1': 'X', 'l2': 'Y',
                              'm1': 'Z', 'm2': 'AA',
                              'n1': 'BB', 'n2': 'CC',
                              'o1': 'DD', 'o2': 'EE'}
            
            if self.four_ply_index == 0:
                self.utility_values = {'P': 16, 'Q': 19,
                                    'R': 14, 'S': 10, 
                                    'T': 13, 'U': 1, 
                                    'V': 10, 'W': 8,
                                    'X': 17, 'Y': 3,
                                    'Z': 15, 'AA': 16,
                                    'BB': 17, 'CC': 19,
                                    'DD': 5, 'EE': 15}

            elif self.four_ply_index == 1:
                self.utility_values = {'P': 19, 'Q': 13,
                                        'R': 4, 'S': 14,
                                        'T': 17, 'U': 13,
                                        'V': 2, 'W': 17,
                                        'X': 3, 'Y': 11, 
                                        'Z': 6, 'AA': 10,
                                        'BB': 22, 'CC': 7, 
                                        'DD': 18, 'EE': 25}
            elif self.four_ply_index == 2:
                self.utility_values = {'P': 23, 'Q': 19,
                                        'R': 23, 'S': 10, 
                                        'T': 27, 'U': 24, 
                                        'V': 9, 'W': 4,
                                        'X': 11, 'Y': 22,
                                        'Z': 8, 'AA': 3,
                                        'BB': 18, 'CC': 20,
                                        'DD': 26, 'EE': 7}
    
    def to_move(self, state):
        return state.ply % self.ply

    def is_terminal(self, state):
        return state.ply == self.ply

    def utility(self, state, player):
        return self.utility_values[state.name]

    def actions(self, state):
        return self.possible_actions[state.name]

    def result(self, state, action):
        name = self.result_of[action]
        newstate = State(name=name, passed_actions=state.passed_actions + [action])
        self.states += [newstate]
        return newstate