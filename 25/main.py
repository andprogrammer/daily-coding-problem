# based on
# https://www.geeksforgeeks.org/wildcard-character-matching/


def match(first, second):
    # If we reach at the end of both strings, we are done
    if not first and not second:
        return True

    # Make sure that the characters after '*' are present
    # in second string. This function assumes that the first
    # string will not contain two consecutive '*'
    if first and first[0] == '*' and not second:
        return False

    # If the first string contains '?', or current characters
    # of both strings match
    if (first and first[0] == '.') or (first and second and first[0] == second[0]):
        return match(first[1:], second[1:])

    # If there is *, then there are two possibilities
    # a) We consider current character of second string
    # b) We ignore current character of second string.
    if first and first[0] == '*':
        return match(first[1:], second) or match(first, second[1:])

    return False


# moje rozwiazanie uwzgledniajace tylko '.'
def check_regex(regex, input):
    if not regex and not input:
        return True
    if regex and not input:
        return False
    if not regex and input:
        return False
    if regex[0] != '.':
        if regex[0] != input[0]:
            return False
    return check_regex(regex[1:], input[1:])


if __name__ == '__main__':
    assert match('ra.', 'ray')
    assert not match('ra.', 'raymond')
    assert match('.*at', 'chat')
    assert not match('.*at', 'chats')

    assert check_regex('.al.ma.kota.', 'DalRmaWkota2')
    assert not check_regex('.al.ma.1kota.', 'DalRmaWkota2')
