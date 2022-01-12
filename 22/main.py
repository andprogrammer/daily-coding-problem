from collections import Counter
def get_original_sentence(s, words):
    if not s or not words:
        return None
    original_sentence = []
    word_found = True
    while s and word_found:
        word_found = False
        for w in words:
            if s.find(w) != -1:
                word_found = True
                original_sentence.append(w)
                s = s.replace(w, '')
    return original_sentence

def compare(x, y):
    return Counter(x) == Counter(y)

if __name__ == '__main__':
    s = 'thequickbrownfox'
    words = ['quick', 'brown', 'the', 'fox']
    assert compare(get_original_sentence(s, words), ['quick', 'brown', 'the', 'fox'])
    s = 'bedbathandbeyond'
    words = ['bed', 'bath', 'bedbath', 'and', 'beyond']
    assert compare(get_original_sentence(s, words), ['bed', 'bath', 'and', 'beyond'])
