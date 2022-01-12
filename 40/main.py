def once(numbers):
    if not numbers:
        return None
    return int((3 * sum(set(numbers)) - sum(numbers)) / 2)


if __name__ == '__main__':
    assert 1 == once([6, 1, 3, 3, 3, 6, 6])
    assert 19 == once([13, 19, 13, 13])
