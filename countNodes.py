class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count(node):
    return count(node.left) + count(node.right) + 1 if node else 0


if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(count(node))
