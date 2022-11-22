from utils import Game, State

def min_value(game, state):
    print(f'Ply: {state.ply}, MAX: node: {state.name}')
    if game.is_terminal(state):
        print(f'Ply: {state.ply}, MAX: node: {state.name} is terminal')
        return (game.utility(state, 1), None)
    inf = float('inf')
    v, move = inf, inf
    for a in game.actions(state):
        print(f'Ply: {state.ply}, MIN: node: {state.name}, tried action {a}')
        v2, a2 = max_value(game, game.result(state, a))
        print(f'Ply: {state.ply}, MIN: node: {state.name}, tried action {a} and the result value is {v2}')
        if v2 < v:
            v, move = v2, a
    print(f'Ply: {state.ply}, MAX: node: {state.name} is done')
    return (v, move)

def max_value(game, state):
    print(f'Ply: {state.ply}, MAX: node: {state.name}')
    if game.is_terminal(state):
        print(f'Ply: {state.ply}, MAX: node: {state.name} is terminal')
        return game.utility(state, 0), None
    m_inf = float('-inf')
    v, move = m_inf, m_inf
    for a in game.actions(state):
        print(f'Ply: {state.ply}, MAX: node: {state.name}, tried action {a}')
        v2, a2 = min_value(game, game.result(state, a))
        print(f'Ply: {state.ply}, MAX: node: {state.name}, tried action {a} and the result value is {v2}')
        if v2 > v:
            v, move = v2, a
    print(f'Ply: {state.ply}, MAX: node: {state.name} is done')
    return (v, move)

def minimax_search(game, state):
    player = game.to_move(state)
    value, move = max_value(game, state)
    return (move, value)


first_state = State('A')
two_ply_game = Game(2, first_state)
four_ply_game1 = Game(4, first_state, 0)
four_ply_game2 = Game(4, first_state, 1)
four_ply_game3 = Game(4, first_state, 2)

game = two_ply_game
print('Best acrion for MAX with the final utility value:', minimax_search(game, first_state))

print()

game = four_ply_game1
print('Best acrion for MAX with the final utility value:', minimax_search(game, first_state))

print()

game = four_ply_game2
print('Best acrion for MAX with the final utility value:', minimax_search(game, first_state))

print()

game = four_ply_game3
print('Best acrion for MAX with the final utility value:', minimax_search(game, first_state))