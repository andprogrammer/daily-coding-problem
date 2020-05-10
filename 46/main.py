def is_palindrome(s):
    if not s:
        return False
    r = s[::-1]
    for x, y in zip(s, r):
        if x != y:
            return False
    return True


def longest_palindromic(s):
    if not s:
        return 0
    if is_palindrome(s):
        return len(s)
    return max(longest_palindromic(s[1:]),
               longest_palindromic(s[:len(s) - 1]))


if __name__ == '__main__':
    print(longest_palindromic('aabcdcb'))
    print(longest_palindromic('aabcdcb'))
    print(longest_palindromic('aabcd'))
