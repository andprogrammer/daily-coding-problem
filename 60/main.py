def f(nums, s):
    if not nums:
        return False
    if s == 0:
        return True
    if s < 0:
        return False
    return f(nums[:-1], s) or f(nums[:-1], s - nums[-1])


def is_possible(n):
    return f(n, sum(n) / 2)


if __name__ == '__main__':
    assert is_possible([15, 5, 20, 10, 35, 15, 10])
    assert not is_possible([15, 5, 20, 10, 35])
    assert is_possible([1, 2, 3, 4, 9, 1])
    assert is_possible([1, 1, 1, 1, 1, 1, 6])
    assert is_possible([5, 6, 4, 7])
    assert not is_possible([5, 6, 4, 8])
    assert is_possible([5, 5, 2, 8])