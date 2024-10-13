import heapq

def astar(graph, start, goal, heuristic):
    # frontier stores tuples of (priority, node)
    frontier = [(heuristic[start], start)]  # (priority, node)
    explored = set()
    cost = {start: 0}
    path = {start: None}

    while frontier:
        # Pop the node with the lowest priority
        current = heapq.heappop(frontier)

        # Check if we've reached the goal
        if current == goal:
            path_list = [current]
            while path[current] is not None:
                path_list.append(path[current])
                current = path[current]

            path_list.reverse()  # Reverse the path to start from 'start'
            return path_list

        explored.add(current)

        # Explore neighbors
        for neighbor in graph[current]:
            new_cost = cost[current] + graph[current][neighbor]
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(frontier, (priority, neighbor))  # Push (priority, neighbor)
                path[neighbor] = current

    return None

# Example graph and heuristic
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'D': 15},
    'C': {'D': 20},
    'D': {}
}

heuristic = {
    'A': 15,
    'B': 10,
    'C': 5,
    'D': 0
}

start = 'A'
goal = 'D'
path = astar(graph, start, goal, heuristic)
print("Shortest path from", start, "to", goal, ":", path)
