def count_decoding(digits, n):
    if n == 0 or n == 1:
        return 1
    count = 0

    if digits[n - 1] > '0':
        count = count_decoding(digits, n - 1)

    if digits[n - 2] == '1' or (digits[n - 2] == '2' and digits[n - 1] < '7'):
        count = count + count_decoding(digits, n - 2)

    return count

if __name__ == '__main__':
    assert count_decoding('111', 3) == 3
    assert count_decoding('1111111', 7) == 21
    