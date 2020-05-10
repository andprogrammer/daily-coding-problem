def foo(data):
    if len(data) == 1:
        return data[0]
    if len(data) == 2:
        return data[0] if data[0] > data[1] else data[1]
    if len(data) & 1:
        return calculate(data)
    first_option = calculate(data)
    second_option = calculate_evens(data)
    return first_option if first_option > second_option else second_option


def calculate(data):
    sum_odd = 0
    sum_even = 0
    index = 0
    while index < len(data):
        sum_odd += data[index]
        index += 2
    index = 1
    while index < len(data):
        sum_even += data[index]
        index += 2
    return sum_odd if sum_odd > sum_even else sum_even


def calculate_evens(data):
    if not data or len(data) == 1:
        raise Exception('Incorrect data')
    if len(data) == 2:
        return data[0] if data[0] > data[1] else data[1]
    if len(data) == 4:
        return data[0] + data[3]
    left_index = 0
    right_index = len(data) - 1
    sum_of_elements = 0
    while left_index + 1 < right_index:
        left_value = data[left_index]
        right_value = data[right_index]
        sum_of_elements += left_value + right_value
        left_index += 2
        right_index -= 2
    left_value = data[left_index]
    right_value = data[right_index]
    sum_of_elements += left_value if left_value > right_value else right_value
    return sum_of_elements


if __name__ == '__main__':
    assert foo([2, 4, 6, 2, 5]) == 13
    assert foo([5, 1, 1, 5]) == 10
