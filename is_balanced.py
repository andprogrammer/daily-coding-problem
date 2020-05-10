def is_pair(left, right):
    if (left == '{' and right == '}') or (left == '[' and right == ']') or (left == '(' and right == ')'):
        return True
    return False


def is_balanced(s):
    if not s:
        return True
    opening = ['{', '[', '(']
    closing = ['}', ']', ')']
    temp_stack = []
    for b in s:
        if b in opening:
            temp_stack.append(b)
        elif b in closing:
            if not temp_stack:
                return False
            top = temp_stack.pop()
            if not is_pair(top, b):
                return False
        else:
            return False
    return True


if __name__ == '__main__':
    assert is_balanced('{[]{()}}')
    assert not is_balanced('[{}{})(]')
    assert is_balanced('{{[[(())]]}}')
    assert not is_balanced('{[(])}')
    assert is_balanced('{[()]}')
