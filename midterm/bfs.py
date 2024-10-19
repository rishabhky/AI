#from typing import Dict

def bfs(graph, node: str) -> None:
    queue = []
    visited = []
    visited.append(node)
    queue.append(node)

    while queue:
        cur_node = queue.pop(0)
        print(cur_node, end=" ")

        for adj_node in graph[cur_node]:
            if adj_node not in visited:
                visited.append(adj_node)
                queue.append(adj_node)


def main():

    # Each `key` represents a parent node, while its `value` represents its adjacent node(s)
    graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": [], "F": []}

    bfs(graph, "A")


if __name__ == "__main__":
    main()

