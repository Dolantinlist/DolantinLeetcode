class Solution:
    def solve(self, board):
        if not board:
            return
        m, n = len(board), len(board[0])
        boarder = [(i, j) for i in range(m) for j in range(n) if i in {0, m - 1} or  j in {0, n - 1}]
        while boarder:
            i, j = boarder.pop()
            if 0<= i <m and 0<=j<n and board[i][j] == 'O':
                board[i][j] = 'S'
                boarder += (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'
        return board


board = [
    ['X','X','X','X'],
    ['X','O','O','X'],
    ['X','X','O','X'],
    ['X','O','X','X']
]
print(Solution().solve(board))
