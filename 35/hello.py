def sortRGB(letters):
    last_R = -1
    ordered_rgb = []
    for i in range(0, len(letters)):
        if letters[i] == 'B':
            ordered_rgb.append('B')
        if letters[i] == 'R':
            ordered_rgb = ['R'] + ordered_rgb
            last_R = 0 if last_R == -1 else last_R + 1
        if letters[i] == 'G':
            if last_R == -1:
                ordered_rgb = ['G'] + ordered_rgb
            else:
                ordered_rgb = ordered_rgb[:last_R + 1] + ['G'] + ordered_rgb[last_R + 1:]
    return ordered_rgb


if __name__ == "__main__":
    print(sortRGB(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
