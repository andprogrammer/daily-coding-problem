def binary_search(numbers, element):
    if not numbers:
        return False
    middle = len(numbers) // 2
    if numbers[middle] == element:
        return True
    elif numbers[middle] > element:
        return binary_search(numbers[:middle], element)
    elif numbers[middle] < element:
        return binary_search(numbers[middle + 1:], element)


def bs(numbers, start, end, element):
    if start == end:
        return start if numbers[start] == element else None
    mid = (end + start) // 2
    if numbers[mid] == element:
        return mid
    elif numbers[mid] > element:
        return bs(numbers, start, mid, element)
    else:
        return bs(numbers, mid + 1, end, element)


if __name__ == '__main__':
    numbers = [55, 45, 34, 12, 78, 565, 3, 7, 2, 9]
    numbers.sort()
    print(numbers)
    assert 2 == bs(numbers, 0, len(numbers), 7)
    assert 9 == bs(numbers, 0, len(numbers), 565)
    assert 4 == bs(numbers, 0, len(numbers), 12)
