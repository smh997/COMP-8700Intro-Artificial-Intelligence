def is_valid(s):
    boat_pos, NO_missionaries , NO_cannibals = s    # position of the boat, number of the missionaries on the other side, number of the cannibals on the other side 
    if NO_missionaries > 3 or NO_cannibals > 3 or NO_missionaries < 0 or NO_cannibals < 0:
        return False
    if boat_pos == 0 and 0 < NO_missionaries < NO_cannibals:
        return False
    elif boat_pos == 1 and 0 < 3 - NO_missionaries < 3 - NO_cannibals:
        return False
    return True

def get_result(state, action):
    return (1 - state[0], state[1] + action[0], state[2] + action[1])

def get_actions(state):
    all_actions = [(1, 0), (0, 1), (1, 1), (0, 2), (2, 0), (-1, 0), (0, -1), (-1, -1), (0, -2), (-2, 0)]

    if state[0] == 0:
        boat_possible_actions = all_actions[:5]
    else:
        boat_possible_actions = all_actions[5:]
    for action in boat_possible_actions:
        if is_valid(get_result(state, action)):
            yield action

# BFS
initial_state = (0, 0, 0)
target = (1, 3, 3)
graph = dict()
bfs_tree = dict()
q = []
q.append(initial_state)
bfs_reached = dict()
bfs_reached[initial_state] = 0

while len(q):
    state = q[0]
    q.pop(0)
    if state not in graph:
        graph[state] = []
        bfs_tree[state] = []
    for action in get_actions(state):
        newstate = get_result(state, action)
        if newstate not in bfs_reached:
            q.append(newstate)
            bfs_reached[newstate] = bfs_reached[state] + 1
            bfs_tree[state].append(newstate)
        graph[state].append(newstate)


# DFS
initial_state = (0, 0, 0)
target = (1, 3, 3)
dfs_tree = dict()
dfs_tree[initial_state] = []
dfs_reached = dict()
dfs_reached[initial_state] = 0

def dfs(state, depth):
    global dfs_tree, dfs_reached
    for action in get_actions(state):
        newstate = get_result(state, action)
        if newstate not in dfs_reached:
            dfs_reached[newstate] = depth
            dfs_tree[newstate] = []
            dfs_tree[state].append(newstate)
            dfs(newstate, depth + 1)

dfs(initial_state, 1)


# Greedy best-first search
import heapq
from functools import cmp_to_key

initial_state = (0, 0, 0)
target = (1, 3, 3)
greedy_reached = dict()
greedy_reached[initial_state] = 0

def h(state):
    global target
    return ((target[1] - state[1]) + (target[2] - state[2])) / 2 #the difference of the number of people of the state and the goal divide by 2 or 1.5 as the capacity of the boat to get the number of moves needed.

def f_greedy(state):
    return h(state)

def add(pq, s):
    heapq.heappush(pq, (f_greedy(s), s))

def pop(pq):
    return heapq.heappop(pq)[1]

def is_goal(state):
    global target
    return state == target

greedy_tree = dict()
frontier = [(f_greedy(initial_state), initial_state)]
heapq.heapify(frontier)

while len(frontier):
    state = pop(frontier)
    if is_goal(state):
        break
    if state not in greedy_tree:
        greedy_tree[state] = []
    for action in get_actions(state):
        newstate = get_result(state, action)
        if newstate not in greedy_reached or greedy_reached[newstate] > greedy_reached[state] + 1 :
            greedy_reached[newstate] = greedy_reached[state] + 1
            add(frontier, newstate)
            greedy_tree[state].append(newstate)


# A*

initial_state = (0, 0, 0)
target = (1, 3, 3)
A_reached = dict()
A_reached[initial_state] = 0


def g_A(state):
    global A_reached
    return A_reached[state] if state in A_reached else 1000

def f_A(state):
    return g_A(state) + h(state)

def add(pq, s):
    heapq.heappush(pq, (f_A(s), s))

A_tree = dict()
frontier = [(f_A(initial_state), initial_state)]
heapq.heapify(frontier)

while len(frontier):
    state = pop(frontier)
    if is_goal(state):
        break
    if state not in A_tree:
        A_tree[state] = []
    for action in get_actions(state):
        newstate = get_result(state, action)
        if newstate not in A_reached or A_reached[newstate] > A_reached[state] + 1 :
            A_reached[newstate] = A_reached[state] + 1
            add(frontier, newstate)
            A_tree[state].append(newstate)

    





# Whole state space:
print('Whole state space:')
for s in graph:
    print(str(s) + ': ' + ', '.join([str(t) for t in graph[s]]))
print()

# Whole graph edges:
print('Whole graph edges:')
for s in graph:
    for nei in graph[s]:
        print(str(s), str(nei))
print()

# BFS Tree edges:
print('BFS Tree edges:')
for s in bfs_tree:
    for nei in bfs_tree[s]:
        print(str(s), str(nei))
print()

# BFS cost of reaching states
print('BFS cost of reaching states:')
for s in bfs_reached:
    print(str(s) + ': ' + str(bfs_reached[s]))
print()

# BFS cost of finding the target
print('BFS cost of finding the target:')
print(str(target) + ': ' + str(bfs_reached[target]))
print()

# DFS Tree edges:
print('DFS Tree edges:')
for s in dfs_tree:
    for nei in dfs_tree[s]:
        print(str(s), str(nei))
print()

# DFS cost of reaching states
print('DFS cost of reaching states:')
for s in dfs_reached:
    print(str(s) + ': ' + str(dfs_reached[s]))
print()

# DFS cost of finding the target
print('DFS cost of finding the target:')
print(str(target) + ': ' + str(dfs_reached[target]))
print()

# Greedy best-first search Tree edges:
print('Greedy best-first search Tree edges:')
for s in greedy_tree:
    for nei in greedy_tree[s]:
        print(str(s), str(nei))
print()

# Greedy best-first search cost of reaching states
print('Greedy best-first search cost of reaching states:')
for s in greedy_reached:
    print(str(s) + ': ' + str(greedy_reached[s]))
print()

# Greedy best-first search cost of finding the target
print('Greedy best-first search cost of finding the target:')
print(str(target) + ': ' + str(greedy_reached[target]))
print()

# A* Tree edges:
print('A* Tree edges:')
for s in A_tree:
    for nei in A_tree[s]:
        print(str(s), str(nei))
print()

# A* cost of reaching states
print('A* cost of reaching states:')
for s in A_reached:
    print(str(s) + ': ' + str(A_reached[s]))
print()

# A* cost of finding the target
print('A* cost of finding the target:')
print(str(target) + ': ' + str(A_reached[target]))
print()