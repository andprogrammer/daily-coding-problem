class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def number_of_paths(m):
    if not m:
        return 0
    stack = [Cell(0, 0)]
    counter = 0
    while stack:
        element = stack.pop()
        if element.x == len(m) - 2:
            counter += 1
        if element.y + 1 < len(m[0]):
            stack.append(Cell(element.x, element.y + 1))
        if element.x + 1 < len(m):
            stack.append(Cell(element.x + 1, element.y))
    return counter


def get_matrix_traversals(num_of_rows, current_row, num_of_columns, current_column):
    if current_row == num_of_rows - 1:
        return 1
    count = 0
    if current_row < num_of_rows - 1:
        count += get_matrix_traversals(num_of_rows, current_row + 1, num_of_columns, current_column)
    if current_column < num_of_columns - 1:
        count += get_matrix_traversals(num_of_rows, current_row, num_of_columns, current_column + 1)
    return count


if __name__ == '__main__':
    assert 2 == get_matrix_traversals(2, 0, 2, 0)
    assert 70 == get_matrix_traversals(5, 0, 5, 0)
    m = [[0 for i in range(3)] for y in range(4)]
    assert 10 == number_of_paths(m)
    m = [[0 for i in range(2)] for y in range(2)]
    assert 2 == number_of_paths(m)
    m = [[0 for i in range(5)] for y in range(5)]
    assert 70 == number_of_paths(m)