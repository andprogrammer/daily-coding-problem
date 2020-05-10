# LRU - least recently used


class Node:
    def __init__(self, key, value):
        self.next = None
        self.prev = None
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + " " + str(self.value)


class LRU:
    def __init__(self, cache_capacity):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache_capacity = cache_capacity
        self.cache_content = dict()

    def _add(self, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node

    def _remove(self, node):
        node_prev = node.prev
        node_next = node.next
        node_prev.next = node_next
        node_next.prev = node_prev
        del node  # TODO is it necessary?

    def set_value(self, key, value):
        if key in self.cache_content:
            node = self.cache_content[key]
            self._remove(node)
            self._add(node)
            return
        if len(self.cache_content) >= self.cache_capacity:
            del self.cache_content[self.tail.prev.key]
            self._remove(self.tail.prev)
        node = Node(key, value)
        self.cache_content[key] = node
        self._add(node)

    def get_value(self, key):
        if key in self.cache_content:
            node = self.cache_content[key]
            self._remove(node)
            self._add(node)
            return node.value
        return None

    def print_cache(self):
        for k, v in self.cache_content.items():
            print(v)

    def print_list(self):
        if self.head.next == self.tail:
            return
        temp = self.head.next
        while temp:
            if temp.key and temp.value:
                print(str(temp.key) + ' ' + str(temp.value))
            temp = temp.next


if __name__ == '__main__':
    lru = LRU(3)
    assert not lru.get_value("a")
    lru.set_value("a", 1)
    assert lru.get_value("a") == 1
    lru.set_value("b", 2)
    lru.set_value("c", 3)

    print('---list---')
    lru.print_list()
    print('---cache---')
    lru.print_cache()

    lru.set_value("d", 4)
    lru.set_value("e", 5)
    lru.set_value("a", 1)

    print('---list---')
    lru.print_list()
    print('---cache---')
    lru.print_cache()

    assert lru.get_value("a") == 1
    assert not lru.get_value("b")
    assert lru.get_value("e") == 5
    assert not lru.get_value("c")
