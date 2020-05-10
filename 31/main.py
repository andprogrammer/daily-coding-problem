# https://lawrencewu.me/2015/02/15/levenshtein-distance.html
def levenshtein(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return max(len(s1), len(s2))

    return min(levenshtein(s1[1:], s2) + 1,
               levenshtein(s1, s2[1:]) + 1,
               levenshtein(s1[1:], s2[1:]) if s1[0] == s2[0]
               else levenshtein(s1[1:], s2[1:]) + 1)


if __name__ == '__main__':
    assert levenshtein('kitten', 'sitting') == 3
