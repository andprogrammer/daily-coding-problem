def maximum_profit(profits):
    best = 0
    i = 0
    while i < len(profits) - 1:
        tmp = max(profits[i + 1:]) - profits[i]
        best = tmp if tmp > best else best
        i += 1
    return best


if __name__ == '__main__':
    assert 5 == maximum_profit([9, 11, 8, 5, 7, 10])
    assert 42 == maximum_profit([9, 11, 8, 50, 7, 10])
