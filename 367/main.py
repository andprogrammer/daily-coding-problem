def get_iterator_numbers(iterator):
    numbers = []
    try:
        while True:
            numbers.append(next(iterator))
    except StopIteration:
        pass
    return numbers


def merge_iterators(x, y):
    iterator_numbers1 = get_iterator_numbers(x)
    iterator_number2 = get_iterator_numbers(y)
    joined = iterator_numbers1 + iterator_number2
    joined.sort()
    return joined


if __name__ == '__main__':
    foo = iter([5, 10, 15])
    bar = iter([3, 8, 9])
    for num in merge_iterators(foo, bar):
        print(num)
