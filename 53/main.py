class Stack:
    def __init__(self):
        self.main_stack = []
        self.backup_stack = []

    def enqueue(self, element):
        self.main_stack.append(element)

    def dequeue(self):
        while self.main_stack:
            self.backup_stack.append(self.main_stack.pop())
        self.backup_stack.pop()
        while self.backup_stack:
            self.main_stack.append(self.backup_stack.pop())

    def __str__(self):
        return str(self.main_stack)


if __name__ == '__main__':
    s = Stack()
    s.enqueue('x')
    s.enqueue('y')
    s.enqueue('z')
    print(s)
    s.dequeue()
    s.dequeue()
    print(s)
