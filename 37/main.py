def kombinacje(mylist, k):
    if k == 0:
        return [None]
    if k == 1:
        return [[x] for x in mylist]
    return [[mylist[i]] + sublist for i in range(len(mylist)) for sublist in kombinacje(mylist[i + 1:], k - 1)]


def podzbiory(mylist):
    def podzbiory_helper(mylist, i):
        if i == len(mylist):
            return kombinacje(mylist, i)
        return kombinacje(mylist, i) + podzbiory_helper(mylist, i + 1)

    return podzbiory_helper(mylist, 0)


if __name__ == '__main__':
    # Permutacja N!
    # ABC -> BCA, CAB, ACB, ...

    # Kombinacja (N/K)=N!/K!(N-K)!
    # ABC -> BC, CA, BA, A, B, C, ...

    print(podzbiory([1, 2, 3]))
    assert len(podzbiory([1, 2, 3, 4])) == 2 ** 4
