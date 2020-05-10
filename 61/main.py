def ipow(base, exp):
    result = 1
    while exp != 0:
        if (exp & 1) == 1:
            result *= base
        exp >>= 1
        base *= base
    return result


if __name__ == '__main__':
    print(ipow(4, 5))
    print(ipow(2, 7))
    print(ipow(3, 7))