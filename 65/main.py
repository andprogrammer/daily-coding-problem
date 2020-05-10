def is_all_visited(visited):
    if not visited:
        return True
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if not visited[i][j]:
                return False
    return True


def print_out_clockwise_spiral(clockwise, direction, x, y, visited):
    if is_all_visited(visited):
        return
    if x == 0 and y == 0:
        print(clockwise[x][y])
        visited[x][y] = True
    if direction == 0:
        if y + 1 < len(clockwise[0]) and not visited[x][y + 1]:
            visited[x][y + 1] = True
            y += 1
            print(clockwise[x][y])
        else:
            direction = 1
    elif direction == 1:
        if x + 1 < len(clockwise) and not visited[x + 1][y]:
            visited[x + 1][y] = True
            x += 1
            print(clockwise[x][y])
        else:
            direction = 2
    elif direction == 2:
        if y - 1 >= 0 and not visited[x][y - 1]:
            visited[x][y - 1] = True
            y -= 1
            print(clockwise[x][y])
        else:
            direction = 3
    elif direction == 3:
        if x - 1 > 0 and not visited[x - 1][y]:
            visited[x - 1][y] = True
            x -= 1
            print(clockwise[x][y])
        else:
            direction = 0
    print_out_clockwise_spiral(clockwise, direction, x, y, visited)


if __name__ == '__main__':
    clockwise = [[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10],
                 [11, 12, 13, 14, 15],
                 [16, 17, 18, 19, 20]]
    visited = [[0 for i in range(len(clockwise[0]))] for j in range(len(clockwise))]
    print_out_clockwise_spiral(clockwise, 0, 0, 0, visited)

    print('-------------')

    clockwise = [[1, 2, 3],
                 [6, 7, 8],
                 [11, 12, 13],
                 [16, 17, 18]]
    visited = [[0 for i in range(len(clockwise[0]))] for j in range(len(clockwise))]
    print_out_clockwise_spiral(clockwise, 0, 0, 0, visited)