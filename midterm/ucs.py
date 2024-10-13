
def uniform_cost_search(start_node,goal_node,graph):
    queue=[(0,start_node)]
    visited=set()

    while queue:
        queue.sort()
        current_cost,current_node=queue.pop(0)

        if current_node==goal_node:
            return current_cost
        
        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor,cost in graph[current_node]:
            if neighbor not in visited:
                new_cost=current_cost+cost
                queue.append((new_cost,neighbor))

    return "Failure: Goal not reachable"

graph={
    'A':[('B',1),('C',4)],
    'B':[('A',1),('D',2),('E',5)],
    'C':[('A',4),('F',3)],
    'D':[('B',2),('G',1)],
    'E':[('B',5),('G',3)],
    'F':[('C',3),('G',2)],
    'G':[('D',1),('E',3),('F',2)]
}

start_node='A'
goal_node='G'

result=uniform_cost_search(start_node,goal_node,graph)
print(f"Cost from {start_node} to {goal_node}: {result}")