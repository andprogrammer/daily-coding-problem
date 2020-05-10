class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def evaluate_tree(node):
    if not node:
        return
    if not node.left and not node.right:
        return int(node.data)
    l = evaluate_tree(node.left)
    r = evaluate_tree(node.right)
    if node.data == '+':
        return l + r
    if node.data == '-':
        return l - r
    if node.data == '*':
        return l * r
    return l / r


if __name__ == '__main__':
    root = Node('*')
    b = Node('+')
    c = Node('+')
    d = Node('3')
    e = Node('2')
    f = Node('4')
    g = Node('5')
    root.left = b
    b.left = d
    b.right = e
    root.right = c
    c.left = f
    c.right = g

    print(evaluate_tree(root))
