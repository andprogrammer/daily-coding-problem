def dfs(board, i, j, visited):
    if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
        return
    if not visited[i][j]:
        visited[i][j] = True
        print(board[i][j])
        dfs(board, i + 1, j, visited)
        dfs(board, i, j + 1, visited)
        dfs(board, i - 1, j, visited)
        dfs(board, i, j - 1, visited)


def main():
    board = [
        ['A', 'B', 'C', 'X'],
        ['D', 'E', 'F', 'Y'],
        ['G', 'H', 'I', 'Z']
    ]
    visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(board, i, j, visited)


if __name__ == '__main__':
    main()
