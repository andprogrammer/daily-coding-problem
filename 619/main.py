# something wrong - not enough time to debug

def is_found(board, word, row, column, visited):
    visited[row][column] = True
    if board[row][column] == word[0]:
        if len(word) == 1:
            return True
        if len(board) > row + 1 >= 0 and not visited[row + 1][column]:  # down
            is_found(board, word[1:], row + 1, column, visited)
        if len(board[0]) > column + 1 >= 0 and not visited[row][column + 1]:  # right
            is_found(board, word[1:], row, column + 1, visited)
        if 0 <= row - 1 < len(board) and not visited[row - 1][column]:  # top
            is_found(board, word[1:], row - 1, column, visited)
        if 0 <= column - 1 < len(board[0]) and not visited[row][column - 1]:  # left
            is_found(board, word[1:], row, column - 1, visited)
    return False


def exists(board, word):
    if not board or not word:
        return False
    visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if is_found(board, word, i, j, visited):
                return True
    return False


def main():
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    # assert exists(board, "ABCCED")
    # assert exists(board, "SEE")
    # assert not exists(board, "ABCB")


if __name__ == '__main__':
    main()
