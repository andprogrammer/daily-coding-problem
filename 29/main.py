def encode(code):
    if not code:
        return ''
    if len(code) == 1:
        return '1' + code
    letter = code[0]
    counter = 1
    encoded = ''
    for i in code[1:]:
        if i != letter:
            encoded += str(counter)
            encoded += letter
            letter = i
            counter = 0
        counter += 1
    encoded += str(counter)
    encoded += letter
    return encoded


def decode(decode):
    if not decode:
        return ''
    if len(decode) < 2:
        raise Exception('Incorrect data')
    code = ''
    counter = 0
    for i in decode:
        if i.isdigit():
            for l in range(0, int(i)):
                code += decode[counter + 1]
        counter += 1
    return code


if __name__ == '__main__':
    assert encode('AAAABBBCCDAA') == '4A3B2C1D2A'
    assert encode('A') == '1A'
    assert encode('') == ''
    assert encode('AABB') == '2A2B'

    assert decode('4A3B2C1D2A') == 'AAAABBBCCDAA'
    assert decode('1A') == 'A'
    assert decode('') == ''
    assert decode('2A2B') == 'AABB'
