class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def dfs(root):
    visited = []

    def _dfs(node):
        if node is None:
            return
        
        visited.append(node.value)
        #print(node.value)

        for child in node.children:
            _dfs(child)
    
    _dfs(root)
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

    visited_nodes = dfs(root)
    print("Visited nodes: ", visited_nodes)