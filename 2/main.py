def no_recursion(numbers):
    output = []
    for i in range(0, len(numbers)):
        internal_dividion = 1
        for j in range(0, len(numbers)):
            if i != j:
                internal_dividion = internal_dividion * numbers[j]
        output.append(internal_dividion)
    return output


def with_recursion(numbers, i, length, j, output, internal_division):
    if i == length:
        return
    if j == length:
        i = i + 1
        j = 0
        output.append(internal_division)
        internal_division = 1
        return with_recursion(numbers, i, length, j, output, internal_division)
    elif numbers[i] != numbers[j]:
        internal_division = internal_division * numbers[j]
    j = j + 1
    return with_recursion(numbers, i, length, j, output, internal_division)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    assert all([a == b for a, b in zip(no_recursion(numbers), [120, 60, 40, 30, 24])])
    numbers = [3, 2, 1]
    assert all([a == b for a, b in zip(no_recursion(numbers), [2, 3, 6])])

    numbers = [1, 2, 3, 4, 5]
    i = 0
    j = 0
    output = []
    internal_dividion = 1
    with_recursion(numbers, i, len(numbers), j, output, internal_dividion)
    assert all([a == b for a, b in zip(output, [120, 60, 40, 30, 24])])

    numbers = [3, 2, 1]
    i = 0
    j = 0
    output = []
    internal_dividion = 1
    with_recursion(numbers, i, len(numbers), j, output, internal_dividion)
    assert all([a == b for a, b in zip(output, [2, 3, 6])])
