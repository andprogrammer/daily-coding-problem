def check_if_dict(data):
    s = ''
    if isinstance(data, dict):
        s += '{'
        for k, v in data.items():
            s += ' {} '.format(k)
            if isinstance(v, dict):
                s += check_if_dict(v)
            elif isinstance(v, list):
                s += check_if_list(v)
            else:
                s += ' {} '.format(v)
        s += '}'
        return s
    return None


def check_if_list(data):
    s = ''
    if isinstance(data, list):
        s += '['
        for x in data:
            if isinstance(x, list):
                s += check_if_list(x)
            elif isinstance(x, dict):
                s += check_if_dict(x)
            else:
                s += ' {} '.format(x)
        s += ']'
        return s
    return None


def get_JSON_encoding(data):
    output = ''
    for x in data:
        if check_if_list(x):
            output += check_if_list(x)
        elif check_if_dict(x):
            output += check_if_dict(x)
        else:
            output += '{} '.format(x)
    return output


if __name__ == '__main__':
    data = [None, 123, ["a", "b"], {"c":"d"}]
    assert get_JSON_encoding(data) == 'None 123 [ a  b ]{ c  d }'
    data = [None, 123, ["a", "b", [4, 5, 6]], {"c": "d", "e": [7, 8]}]
    assert get_JSON_encoding(data) == 'None 123 [ a  b [ 4  5  6 ]]{ c  d  e [ 7  8 ]}'
