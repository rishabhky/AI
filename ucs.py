from queue import PriorityQueue
def uniform_cost_search(start_node, goal_node, graph):
    frontier=PriorityQueue()
    frontier.put((0,start_node))
    explored=set()
    path=[]

    while not frontier.empty():
        current_cost,current_node=frontier.get()
        path.append(current_node)

        if current_node==goal_node:
            return f"Goal reached with cost:{current_cost} Path:{path}"
        explored.add(current_node)
        for neighbor, cost in graph[current_node].items():
            if neighbor not in explored:
                new_cost=current_cost+cost
                frontier.put((new_cost,neighbor)) 

    return "Goal not reachable"

graph={
    'A':{'B':1, 'C':4},
    'B':{'A':1,'D':2,'E':5},
    'C':{'A':4,'F':3},
    'D':{'B':2},
    'E':{'B':5,'F':1},
    'F':{'C':3,'E':1}
}

start_node='A'
goal_node='F'

result=uniform_cost_search(start_node,goal_node,graph)
print(result)