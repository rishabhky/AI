from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def bfs(root):
    if root is None:
        return []

    visited = []
    queue = deque([root])  # Use a deque as a queue for BFS

    while queue:
        node = queue.popleft()  # Remove the node from the front of the queue
        visited.append(node.value)  # Process the node
        # Add all children of the node to the queue
        for child in node.children:
            queue.append(child)

    return visited

if __name__ == "__main__":
    root = TreeNode(1)
    child1 = TreeNode(2)
    child2 = TreeNode(3)
    child3 = TreeNode(4)
    child4 = TreeNode(5)
    child5 = TreeNode(6)

    root.children.append(child1)
    root.children.append(child2)
    child1.children.append(child3)
    child1.children.append(child4)
    child2.children.append(child5)

    visited_nodes = bfs(root)
    print("Visited nodes: ", visited_nodes)
