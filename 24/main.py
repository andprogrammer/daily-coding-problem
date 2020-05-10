# ewentualnie rozwiazanie:
# https://github.com/subsr97/daily-coding-problem/blob/master/challenges/locking-in-binary-tree.py#L21


class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.locked = False
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def is_locked(self):
        return self.locked

    def ancestors_not_locked(self):
        if self.locked:
            return False
        if not self.parent:
            return True
        return self.parent.ancestors_not_locked()

    def descendants_not_locked(self):
        if self.locked:
            return False
        l = None
        r = None
        if self.left:
            l = self.left.descendants_not_locked()
        if self.right:
            r = self.right.descendants_not_locked()
        if self.left and self.right:
            return l and r
        if self.left:
            return l
        if self.right:
            return r
        return True

    def lock(self):
        if self.is_locked():
            return False
        if self.ancestors_not_locked() and self.descendants_not_locked():
            self.locked = True
            return True
        return False

    def unlock(self):
        if not self.is_locked():
            return False
        if (not self.parent or self.parent.ancestors_not_locked()) or (
                (not self.left or self.left.descendants_not_locked()) and (
                not self.right or self.right.descendants_not_locked())):
            self.locked = False
            return True
        return False


if __name__ == '__main__':
    """
           4
          / \
         2   5
        / \
       1   3
      /
     0
    """

    zero = Node(0)
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)

    four.left = two
    two.parent = four

    four.right = five
    five.parent = four

    two.left = one
    one.parent = two

    two.right = three
    three.parent = two

    one.left = zero
    zero.parent = one

    assert one.ancestors_not_locked()
    assert two.descendants_not_locked()

    zero.locked = True
    assert not two.descendants_not_locked()
    assert two.ancestors_not_locked()
    assert three.descendants_not_locked()

    two.locked = True
    assert not one.ancestors_not_locked()
    assert not zero.ancestors_not_locked()

    assert not one.lock()
    assert five.lock()
    assert five.unlock()
