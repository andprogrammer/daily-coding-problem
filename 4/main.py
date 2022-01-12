def foo(nums):
    sorted_nums = sorted(nums)
    one_before = -99999
    for i in sorted_nums:
        if i > 0:
            if one_before > 0:
                new_number = one_before + 1
                if new_number < i:
                    return new_number
                else:
                    one_before = i
                    continue
            new_number = 1
            if i > new_number:
                return new_number
        one_before = i
    return one_before + 1 if one_before > 0 else 1

if __name__ == '__main__':
    assert foo([3, 4, -1, 1]) == 2
    assert foo([1, 2, 0]) == 3
    assert foo([-1, 1, 1, 2]) == 3
    assert foo([-1, 0, 1, 2, 2, 2]) == 3
