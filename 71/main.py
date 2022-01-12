from random import randint


def rand7():
    return randint(1, 7)


def rand5():
    return rand7() % 5 + 1


if __name__ == '__main__':
    print(rand5())
