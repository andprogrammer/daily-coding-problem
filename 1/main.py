def f(elements, k):
    elements = sorted(elements)
    len_input = len(elements)
    start = 0
    end = len_input - 1
    while start < len_input and end >= 0 and start < end:
        sum_of_pair = elements[start] + elements[end]
        if sum_of_pair == k:
            return True
        elif sum_of_pair < k:
            start = start + 1
        else:
            end = end - 1
    return False


if __name__ == '__main__':
    numbers = [10, 15, 3, 7]
    k = 17
    assert f(numbers, k) == True
    k = 22
    assert f(numbers, k) == True
    k = 11
    assert f(numbers, k) == False
