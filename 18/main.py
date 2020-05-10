def foo(arr, k):
    if not 1 <= k <= len(arr):
        raise Exception("Incorrect data")
    start = 0
    end = k
    output = []
    while end <= len(arr):
        output.append(max(arr[start:end]))
        start += 1
        end += 1
    return output


if __name__ == '__main__':
    assert foo([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8]
