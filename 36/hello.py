class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return "root={0} left={1} right={2}".format(self.data, self.left, self.right)


def inorder(node, visited):
    if not node:
        return None
    inorder(node.left, visited)
    visited.append(node.data)
    inorder(node.right, visited)


def penultimate(node):
    visited = []
    inorder(node, visited)
    print(visited)
    if visited and len(visited) > 1:
        return visited[-2]
    if visited:
        return visited[0]
    return None


if __name__ == "__main__":
    n = Node(4)
    n.left = Node(2)
    n.right = Node(6)
    print(penultimate(n))
