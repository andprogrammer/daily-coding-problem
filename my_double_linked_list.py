# DLL - double linked list


class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value

    def __str__(self):
        return str(self.value)


class DLL:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node

    def remove(self, node):
        node_prev = node.prev
        node_next = node.next
        node_prev.next = node_next
        node_next.prev = node_prev
        del node  # TODO is it necessary?

    def print_list(self):
        if self.head.next == self.tail:
            return
        temp = self.head.next
        while temp:
            print(str(temp.value))
            temp = temp.next


if __name__ == '__main__':
    a = Node(2)
    b = Node(4)
    c = Node(8)

    dll = DLL()
    dll.add(a)
    dll.add(b)
    dll.add(c)
    dll.print_list()
    dll.remove(b)
    dll.print_list()
