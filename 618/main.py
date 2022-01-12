from random import randrange


def get_max_index(l, i, j):
    curr_max = -9999
    index = -1
    for x in range(i, j):
        if curr_max < l[x]:
            curr_max = l[x]
            index = x
    return index


def s(l):
    curr_last_index = len(l)
    while curr_last_index > 1:
        max_index = get_max_index(l, 0, curr_last_index)
        flip(l, max_index, curr_last_index - 1)
        curr_last_index -= 1


def flip(l, i, j):
    while i < j:
        tmp = l[i]
        l[i] = l[j]
        l[j] = tmp
        i += 1
        j -= 1


def main():
    l = [randrange(100) for i in range(0, 10)]
    s(l)
    print(l)


if __name__ == '__main__':
    main()
