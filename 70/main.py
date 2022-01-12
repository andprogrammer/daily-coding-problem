def get_perfect_number(number):
    primary_sum = 0
    for char in str(number):
        primary_sum += int(char)
    difference = 10 - primary_sum
    return int(str(number) + str(difference))


if __name__ == '__main__':
    assert get_perfect_number(7) == 73
    assert get_perfect_number(1) == 19
    assert get_perfect_number(2) == 28
    assert get_perfect_number(3) == 37
    assert get_perfect_number(10) == 109
    assert get_perfect_number(11) == 118
    assert get_perfect_number(19) == 190
