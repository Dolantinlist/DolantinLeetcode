class Solution(object):
    def solveSudoku(self,board):
        self.board = board
        self.solve()

    def solve(self):
        row, col = self.find_empty()
        if row == -1 & col == -1:
            return True
        else:
            for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if self.is_safe(row, col, num):
                    self.board[row][col] = num
                    if self.solve():
                        return True
                    else:
                        self.board[row][col] = '.'

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    return i, j
        return -1, -1

    def is_safe(self, row, col, num):
        boxcol = col - col % 3
        boxrow = row - row % 3
        if self.check_row(row, num) & self.check_col(col, num) & self.check_box(boxrow, boxcol, num):
            return True
        return False

    def check_row(self, row, num):
        for i in range(9):
            if self.board[row][i] == num:
                return False
        return True

    def check_col(self, col, num):
        for i in range(9):
            if self.board[i][col] == num:
                return False
        return True

    def check_box(self, boxrow, boxcol, num):
        for i in range(boxrow, boxrow + 3):
            for j in range(boxcol, boxcol + 3):
                if self.board[i][j] == num:
                    return False
        return True