# O(N^3) not optimal solution
def max_product(numbers):
    if len(numbers) < 3:
        return
    max_value = 0
    for i in range(len(numbers) - 2):
        for j in range(i, len(numbers) - 1):
            for k in range(j, len(numbers)):
                max_value = max(max_value, numbers[i] * numbers[j] * numbers[k])
    return max_value


if __name__ == '__main__':
    assert 500 == max_product([-10, -10, 5, 2])
    assert 100 == get_largest_product([-10, 10, 5, 2])
