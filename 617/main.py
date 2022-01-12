def value():
    return {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }


def roman_to_int(s):
    i = 0
    result = 0
    while i < len(s):
        current = s[i]
        if i + 1 < len(s):
            if value()[current] >= value()[s[i + 1]]:
                result += value()[current]
                i += 1
            else:
                result += value()[s[i + 1]] - value()[current]
                i += 2
        else:
            result += value()[current]
            i += 1
    return result


def main():
    assert 4 == roman_to_int('IV')
    assert 14 == roman_to_int('XIV')
    assert 3 == roman_to_int('III')
    assert 19 == roman_to_int('XIX')
    assert 1904 == roman_to_int('MCMIV')


if __name__ == '__main__':
    main()
