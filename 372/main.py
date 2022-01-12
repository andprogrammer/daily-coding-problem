def get_number_of_digits(number):
    return len(str(number))


def get_num_of_digits(number):
    if not number:
        return 0
    return 1 + get_num_of_digits(number // 10)


if __name__ == '__main__':
    assert 4 == get_number_of_digits(1028)
    assert 4 == get_num_of_digits(1028)