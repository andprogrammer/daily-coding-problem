def embolden(s, lst):
    bold = [False for i in range(len(s))]
    for x in lst:
        for i in range(len(s) - len(x) + 1):
            if s[i:i + len(x)] == x:
                for j in range(i, i + len(x)):
                    bold[j] = True
    output = ''
    i = 0
    while i < len(bold):
        if bold[i]:
            output += '<b>'
            while bold[i] and i < len(bold):
                output += s[i]
                i += 1
            output += '</b>'
            continue
        else:
            #     output += '<b>'
            output += s[i]
            #     output += '</b>'
        i += 1
    return output


if __name__ == '__main__':
    s = 'abcdefg'
    lst = ["bc", "ef"]
    assert embolden(s, lst) == 'a<b>bc</b>d<b>ef</b>g'
    s = 'abcdefg'
    lst = ["bcd", "def"]
    assert embolden(s, lst) == 'a<b>bcdef</b>g'
