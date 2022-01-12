# similar problem
def check_if_visited(visited, element):
    if not visited:
        return False
    if not element:
        return False
    return True if element in visited else False


def check_if_path_exists(matrix):
    if not matrix:
        return False
    n = len(matrix)
    m = len(matrix[0])
    stack = []
    for i in range(m):
        if matrix[0][i]:
            stack.append((0, i))

    visited = []

    while stack:
        h, w = stack.pop()
        elem = (h, w)
        if (h + 1) < n:
            if matrix[h + 1][w] and not check_if_visited(visited, elem):  # bottom
                stack.append((h + 1, w))
                visited.append((h, w))
            elif (w - 1) >= 0 and (matrix[h][w - 1]) and not check_if_visited(visited, elem):  # left
                stack.append((h, w - 1))
                visited.append((h, w))
            elif (w + 1) < m and (matrix[h][w + 1]) and not check_if_visited(visited, elem):  # right
                stack.append((h, w + 1))
                visited.append((h, w))
        else:
            return True
    return False


if __name__ == '__main__':
    matrix = [[1, 0, 1, 0, 0],
              [1, 0, 1, 1, 1],
              [0, 1, 1, 0, 1],
              [0, 1, 0, 1, 1]]
    assert check_if_path_exists(matrix)

    matrix = [[1, 0, 1, 0, 0],
              [1, 0, 1, 1, 1],
              [0, 1, 1, 0, 1],
              [0, 0, 0, 1, 1]]
    assert not check_if_path_exists(matrix)

    matrix = [[1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [0, 0, 0, 1, 1]]
    assert check_if_path_exists(matrix)

    matrix = [[0, 0, 0, 0, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [0, 0, 0, 1, 0]]
    assert check_if_path_exists(matrix)

    matrix = [[0, 0, 0],
              [1, 1, 1],
              [1, 1, 1],
              [0, 0, 1]]
    assert not check_if_path_exists(matrix)

    matrix = [[0, 1, 0],
              [1, 1, 1],
              [1, 1, 1]]
    assert check_if_path_exists(matrix)

    matrix = [[0, 0, 0, 1, 0],
              [1, 1, 1, 1, 1],
              [1, 1, 0, 0, 1],
              [0, 1, 0, 1, 1]]
    assert check_if_path_exists(matrix)
