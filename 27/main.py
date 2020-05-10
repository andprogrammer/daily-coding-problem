# check if string is balanced
# time complexity O(N)
# memory complexity (pessimistic) O(N/2) -> O(N)


def opening_bracket(bracket):
    return bracket == '(' or bracket == '[' or bracket == '{'


def same_bracket_type(left, right):
    return (left == '(' and right == ')') or (left == '[' and right == ']') or (left == '{' and right == '}')


def valid_bracket(bracket):
    return bracket == '(' or bracket == '[' or '{'


def is_balanced(input):
    if not input:
        return True
    stack = []
    for i in input:
        if not valid_bracket(i):
            return False
        if opening_bracket(i):
            stack.append(i)
        else:
            if len(stack):
                last = stack[-1]
                if not opening_bracket(last) or not same_bracket_type(last, i):
                    return False
                stack.pop()
            else:
                return False
    return len(stack) == 0


# recursively solution is not correct
def is_balanced_recursively(input, before):
    if not input:
        return True
    if not valid_bracket(before):
        return False
    first = input[0]
    print(first)
    if opening_bracket(first):
        return is_balanced_recursively(input[1:], first)
    return same_bracket_type(before, first)


if __name__ == '__main__':
    assert is_balanced('([])[]({})')
    assert not is_balanced('([)]')
    assert not is_balanced('((()')
