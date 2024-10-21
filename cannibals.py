def valid(state):
    # Check if the state is valid (no missionaries eaten)
    if state[0][0] < state[0][1] and state[0][0] > 0:  # Left bank
        return False
    if state[1][0] < state[1][1] and state[1][0] > 0:  # Right bank
        return False
    return True

def successors(state):
    children = []
    # Try all possible moves of missionaries and cannibals
    for i in range(3):
        for j in range(3):
            if i + j < 1 or i + j > 2:  # Boat must carry 1 or 2 people
                continue
            if state[2] == 1:  # If the boat is on the left side
                child = ((state[0][0] - i, state[0][1] - j), (state[1][0] + i, state[1][1] + j), 0)
            else:  # If the boat is on the right side
                child = ((state[0][0] + i, state[0][1] + j), (state[1][0] - i, state[1][1] - j), 1)
            
            # If the child state is valid, add it to the children list
            if valid(child):
                children.append(child)
    
    return children

def bfs(start, goal):
    visited = set()  # Using a set for faster membership checking
    queue = [[start]]  # Queue to store paths
    
    while queue:
        path = queue.pop(0)  # Get the first path from the queue
        node = path[-1]  # Get the last state from the path
        
        # If the goal is reached, return the path
        if node == goal:
            return path
        
        # Explore successors of the current state
        for child in successors(node):
            if child not in visited:
                visited.add(child)  # Mark the child as visited
                new_path = list(path)  # Create a new path
                new_path.append(child)  # Add the child to the path
                queue.append(new_path)  # Add the new path to the queue
    
    return []  # No solution found

# Define the initial and goal states
initial = ((3, 3), (0, 0), 1)  # (missionaries, cannibals) on left and right, boat on the left
goal = ((0, 0), (3, 3), 0)  # Goal state with all on the right and boat on the right

# Find the path using BFS
path = bfs(initial, goal)

# Print the solution path if found
if path:
    for state in path:
        print(state)
else:
    print("No solution found.")
