def get_all_substring_of_string(string):
    j = 1
    a = set()
    while True:
        for i in range(len(string) - j + 1):
            a.add(string[i:i + j])
        if j == len(string):
            break
        j += 1
    return a


def get_longest_string(data, k):
    longest_string = 0
    for i in data:
        counter = 0
        letters = []
        for j in i:
            counter += 1
            if j not in letters:
                if len(letters) >= k:
                    counter = 0
                    break
                letters.append(j)
        longest_string = counter if counter > longest_string else longest_string
    return longest_string


print(get_longest_string(get_all_substring_of_string('abcba'), k=2))
