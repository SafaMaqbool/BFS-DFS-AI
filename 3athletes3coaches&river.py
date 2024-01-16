import copy
#using dfs approach
# Define the initial and goal states
initial_state = {'left': ['C', 'C', 'C', 'A', 'A', 'A'], 'right': []}
goal_state = {'left': [], 'right': ['C', 'C', 'C', 'A', 'A', 'A']}

def is_valid_state(state):
    left = state['left']
    right = state['right']

    # Check if athletes outnumber coaches on either bank
    if 'A' in left and 'C' in left and len(left[left.index('A'):]) > len(left[left.index('C'):]):
        return False
    if 'A' in right and 'C' in right and len(right[right.index('A'):]) > len(right[right.index('C'):]):
        return False

    return True

def is_goal_state(state):
    return state == goal_state

def print_state(state):
    left = state['left']
    right = state['right']
    print("Left Bank:", left)
    print("Right Bank:", right)
    print("\n")

def river_crossing_puzzle(initial_state):
    stack = [initial_state]

    while stack:
        current_state = stack.pop()
        if is_goal_state(current_state):
            print("Puzzle Solved!")
            print_state(current_state)
            return

        if is_valid_state(current_state):
            for person in current_state['left']:
                new_state = copy.deepcopy(current_state)
                new_state['left'].remove(person)
                new_state['right'].append(person)
                stack.append(new_state)

river_crossing_puzzle(initial_state)
