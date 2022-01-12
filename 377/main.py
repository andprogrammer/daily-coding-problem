def is_odd(number):
    return number & 1


def get_median(data):
    sorted_data = sorted(data)
    if is_odd(len(sorted_data)):
        return sorted_data[len(sorted_data) // 2]
    else:
        middle_index = len(sorted_data) // 2
        return (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2


def get_median_of_k_elements(data, k):
    curr_index = 0
    if k <= len(data):
        while curr_index + k <= len(data):
            curr_data = data[curr_index:curr_index + k]
            print('{} <- median of {}'.format(get_median(curr_data), curr_data))
            curr_index += 1


if __name__ == '__main__':
    data = [-1, 5, 13, 8, 2, 3, 3, 1]
    get_median_of_k_elements(data, 3)
