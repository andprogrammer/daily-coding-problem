# remove_kth_from_end()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_l(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def print_list(self, node):
        if not node:
            return
        if node:
            print(node.data)
        self.print_list(node.next)


i = 0


def remove_kth_from_end(node, k):
    global i
    i = 0
    if not node:
        return
    node.data = 67
    remove_kth_from_end(node.next, k)
    i += 1
    if i == k:
        print(node.data)


if __name__ == '__main__':
    zero = Node(0)
    one = Node(1)
    two = Node(2)

    zero.next = one
    one.next = two

    ll = LinkedList()
    ll.head = zero

    ll.print_list(ll.head)
    ll.print_l()
    remove_kth_from_end(ll.head, 4)
