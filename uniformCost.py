def uniform_cost_search(graph, start, goal):
    queue = [(0, start)]
    visited = set()

    while queue:
        queue.sort()
        current_cost, current_node = queue.pop(0)
        if current_node == goal:
            return current_cost
        
        if current_node in visited:
            continue

        visited.add(current_node)
        
        for neighbour, cost in graph[current_node]:
            if neighbour not in visited:
                total_cost = current_cost + cost
                queue.append((total_cost, neighbour))
    
    return "Failure: Goal not reachable from start"

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2), ('G', 1)],
    'E': [('B', 5), ('G', 3)],
    'F': [('C', 3), ('G', 2)],
    'G': [('D', 1), ('E', 3), ('F', 2)]
}

# Test the UCS function
start_node = 'A'
goal_node = 'G'
result = uniform_cost_search(graph, start_node, goal_node)
print(f"Cost from {start_node} to {goal_node}: {result}")