#from typing import List, Dict


def dfs(graph, start, stack):
    visited = []

    visited.append(start)
    stack.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, stack)


def main():

    # Each `key` represents a parent node, while its `value` represents its adjacent node(s)
    graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": [], "F": []}

    stack = []

    dfs(graph, "A", stack)

    print(stack)


if __name__ == "__main__":
    main()

