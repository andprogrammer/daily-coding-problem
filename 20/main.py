class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_node(self, data):
        new = Node(data, self.head)
        self.head = new

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next


def find_intersecting_node(x, y):
    if not x or not y:
        raise Exception('Incorrect data')
    a = x.head
    b = y.head
    while a:
        temp = b
        while a and temp and a.data != temp.data:
            temp = temp.next
        if temp:
            l = a
            value = l.data
            while l and temp and l.data == temp.data:
                l = l.next
                temp = temp.next
            if not l:
                return value
        a = a.next
    return -1


if __name__ == '__main__':
    head = Node(10)
    x = LinkedList(head)
    x.add_node(8)
    x.add_node(7)
    x.add_node(3)

    head = Node(10)
    y = LinkedList(head)
    y.add_node(8)
    y.add_node(1)
    y.add_node(99)

    assert find_intersecting_node(x, y) == 8
