# helpfully
# https://www.youtube.com/watch?v=VmogG01IjYc


class PriorityQueue:
    def __init__(self, reverse=False):
        self.data = []
        self.reverse = reverse

    def add(self, number):
        self.data.append(number)

    def poll(self):
        if self.data:
            self.data.sort()
            return self.data.pop(0)
        return None

    def peek(self):
        if not self.data:
            return None
        self.data.sort(reverse=self.reverse)
        if self.data:
            return self.data[0]

    def size(self):
        return len(self.data)


def add_number(number, lowers, highers):
    if not lowers or (lowers.data and number < lowers.peek()):
        lowers.add(number)
    else:
        highers.add(number)


def rebalance(lowers, highers):
    bigger_heap = lowers if lowers.size() > highers.size() else highers
    smaller_heap = highers if lowers.size() > highers.size() else lowers

    if bigger_heap.size() - smaller_heap.size() >= 2:
        smaller_heap.add(highers.poll())


def get_median(lowers, highers):
    bigger_heap = lowers if lowers.size() > highers.size() else highers
    smaller_heap = highers if lowers.size() > highers.size() else lowers

    if bigger_heap.size() == smaller_heap.size():
        return float(bigger_heap.peek() + smaller_heap.peek()) / 2.
    return float(bigger_heap.peek())


def get_medians(array):
    lowers = PriorityQueue(True)
    highers = PriorityQueue()
    medians = []
    i = 0
    while i < len(array):
        number = array[i]
        add_number(number, lowers, highers)

        rebalance(lowers, highers)
        medians.append(get_median(lowers, highers))
        i += 1
    return medians


def check(l, r):
    return len(l) == len(r) and sorted(l) == sorted(r)


if __name__ == '__main__':
    assert check(get_medians([2, 1, 5, 7, 2, 0, 5]),  [2.0, 1.5, 2.0, 3.5, 2.0, 2.0, 2.0])
