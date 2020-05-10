def foo(word, dictionary):
    return [x for x in dictionary if x[:len(word)] == word]


if __name__ == '__main__':
    print(foo('de', ['dog', 'deer', 'deal']))
