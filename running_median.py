class Heap:
    def __init__(self, top_greatest=True):
        self.container = []
        self.topGreatest = top_greatest

    def push(self, number):
        self.container.append(number)
        self.container.sort()
        if self.topGreatest:
            self.container = self.container[::-1]

    def top(self):
        if not self.container:
            return
        return self.container[0]

    def remove_top(self):
        if self.container:
            self.container.pop(0)

    def size(self):
        return len(self.container)


def running_median(numbers):
    if not numbers:
        return
    current_median = numbers[0]
    hmax = Heap()
    hmin = Heap(False)
    for i in numbers:
        if i < current_median:
            hmax.push(i)
        else:
            hmin.push(i)
        if abs(hmax.size() - hmin.size()) > 1:
            if hmax.size() > hmin.size():
                top = hmax.top()
                hmax.remove_top()
                hmin.push(top)
            else:
                top = hmin.top()
                hmin.remove_top()
                hmax.push(top)
        if hmax.size() == hmin.size():
            if hmax.size() > 0:  # or hmin.size()
                current_median = (hmax.top() + hmin.top()) / 2
                print(current_median)
        elif hmax.size() > hmin.size():
            current_median = hmax.top()
            print(current_median)
        else:
            current_median = hmin.top()
            print(current_median)


if __name__ == '__main__':
    running_median([12, 4, 5, 3, 8, 7])