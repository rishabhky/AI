import random
def hill_climbing_search(f,neighbor_fn,max_iter=1000):
    current=random.choice(list(x_range))
    for i in range(max_iter):
        neighbors=neighbor_fn(current)
        next_neighbor=max(neighbors,key=lambda x:f(x))
        if f(next_neighbor)<=f(current):
            break
        current=next_neighbor
    return current,f(current)

def f(x):
    return -x**2
def neighbor_fn(x):
    return [x+dx for dx in[-0.1,0,0.1]]
x_range=[x for x in range(10)]
best_solution,best_value=hill_climbing_search(f, neighbor_fn)
print("Best solution: x=",best_solution,"Best value: f(x)=", -best_value)