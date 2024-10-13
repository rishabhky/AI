import heapq
def astar(graph,start,goal,heuristic):
    frontier=[(heuristic[start],start)]
    explored=set()
    cost={start:0}
    path={start:None}

    while frontier:
        current=heapq.heappop(frontier)
        if current==goal:
            path_list=[current]
            while path[current]!=None:
                path_list.append(path[current])
                current=path[current]

            path_list.reverse()
            return path_list
        
        explored.add(current)

        for neighbor in graph[current]:
            new_cost=cost[current]+graph[current][neighbor]
            if neighbor not in cost or new_cost<cost[neighbor]:
                cost[neighbor]=new_cost
                priority=new_cost+heuristic[neighbor]
                heapq.heappush(frontier,(priority,neighbor))
                path[neighbor]=current
    return None

graph={
    'A':{'B':5,'C':10},
    'B':{'D':15},
    'C':{'D':20},'D':{}
}

heuristic={
    'A':15,
    'B':10,
    'C':5,
    'D':0
}

start='A'
goal='D'
path=astar(graph,start,goal,heuristic)
print("shortest path from",start,"to",goal,":",path)
