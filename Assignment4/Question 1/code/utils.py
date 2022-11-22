from math import log, ceil
class State:

    def __init__(self, name, passed_actions=[]):
        self.name = name
        self.passed_actions = passed_actions
        self.ply = len(self.passed_actions)

class Game:
    def __init__(self, ply, root_state, four_ply_index=0):
        self.ply = ply
        self.states = [root_state]
        self.possible_actions = []
        if self.ply == 2:
            self.possible_actions = {'A': ['a1', 'a2', 'a3'],
                                     'B': ['b1', 'b2', 'b3'], 'C': ['c1', 'c2', 'c3'], 'D': ['d1', 'd2', 'd3']}
            self.result_of = {'a1': 'B', 'a2': 'C', 'a3': 'D', 
                              'b1': 'E', 'b2': 'F', 'b3': 'G', 
                              'c1': 'H', 'c2': 'I', 'c3': 'J', 
                              'd1': 'K', 'd2': 'L', 'd3': 'M'}
            self.utility_values = {('a1', 'b1'): 3, ('a1', 'b2'): 12, ('a1', 'b3'): 8,
                                   ('a2', 'c1'): 2, ('a2', 'c2'): 4, ('a2', 'c3'): 6,
                                   ('a3', 'd1'): 14, ('a3', 'd2'): 5, ('a3', 'd3'): 2}
        elif self.four_ply_index == 0:
            pass
        elif self.four_ply_index == 1:
            pass
        elif self.four_ply_index == 2:
            pass
    
    def to_move(self, state):
        return state.ply % self.ply

    def is_terminal(self, state):
        return state.ply == self.ply

    def utility(self, state, player):
        if self.ply == 2:
            return self.utility_values[tuple(state.passed_actions)]
        else:
            pass

    def actions(self, state):
        return self.possible_actions[state.name]

    def result(self, state, action):
        name = self.result_of[action]
        newstate = State(name=name, passed_actions=state.passed_actions + [action])
        self.states += [newstate]
        return newstate