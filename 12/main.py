def staircase(n):
    if n <= 1:
        return 1
    return staircase(n - 1) + staircase(n - 2)

if __name__ == '__main__':
    assert staircase(1) == 1
    assert staircase(2) == 2
    assert staircase(3) == 3
    assert staircase(4) == 5
