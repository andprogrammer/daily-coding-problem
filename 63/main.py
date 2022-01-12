def word_exists(words, word):
    if not word or (not words and not word):
        return True
    if not words and word:
        return False
    for x in words:
        if ''.join(x) == word:
            return True
    for i in range(len(words)):
        w = ''
        for j in range(len(words[0])):
            w += words[j][i]
        if w == word:
            return True
    return False


if __name__ == '__main__':
    matrix = [['F', 'A', 'C', 'I'],
              ['O', 'B', 'Q', 'P'],
              ['A', 'N', 'O', 'B'],
              ['M', 'A', 'S', 'S']]
    assert not word_exists(matrix, "FOAMS")
    assert word_exists(matrix, "FOAM")
    assert word_exists(matrix, "MASS")
    assert not word_exists(matrix, "FORM")