# https://stackoverflow.com/questions/53517687/tricky-way-to-split-string-by-t?noredirect=1#comment93906005_53517687


def get_longest_path(path):
    joined_things = join_the_things_back_together(path)
    counter, index = get_inmost_file_and_index(joined_things)
    out = get_whole_path(counter, index, joined_things)
    return get_path_length(out)


def join_the_things_back_together(path):
    l = [[]]
    for c in path:
        if c != "\t":
            l[-1].append(c)
        elif l[-1][-1] == "\t":
            l[-1].append(c)
        else:
            l.append([])
            l[-1].append(c)
    return [''.join(elem) for elem in l]


def get_path_length(out):
    t = list(map(lambda x: x.replace('\t', ''), out))
    e = ''.join(t)
    return len(e) + len(t) - 1


def get_whole_path(counter, index, l):
    out = [l[index]]
    if index > 0:
        while index >= 0:
            index -= 1
            if l[index].count('\t') < counter:
                counter -= 1
                out.append(l[index])
    return out


def get_inmost_file_and_index(l):
    counter = 0
    index = -1
    for i in range(0, len(l)):
        c = l[i].count('\t')
        if c > counter:
            counter = c
            index = i
    return counter, index


if __name__ == '__main__':
    path = "dir\tsubdir1\t\tfile1.ext\t\tsubsubdir1\tsubdir2\t\tsubsubdir2\t\t\tfile2.ext"
    assert get_longest_path(path) == 32
