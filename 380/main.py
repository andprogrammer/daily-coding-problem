def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    current = 0
    dividing_counter = 0
    while current + y < x:
        dividing_counter += 1
        current += y
    second = x - current if x != current else 0
    return dividing_counter, second


if __name__ == '__main__':
    assert divide(10, 3) == (3, 1)
    assert divide(31, 5) == (6, 1)
