class Solution(object):
    def is_valid_sudoku(self, board):


        for i in range(9):
            dict = {}
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in dict.keys():
                        return False
                    else:
                        dict[board[i][j]] = 1


        for j in range(9):
            dict = {}
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in dict.keys():
                        return False
                    else:
                        dict[board[i][j]] = 1

        for i in range(3):
            for j in range(3):
                dict = {}
                print(" ")
                for k in range(3):
                    for h in range(3):
                        print(3 * i + k, 3 * j + h)
                        if board[3 * i + k][3 * j + h] != '.':
                            if board[3 * i + k][3 * j + h] in dict.keys():
                                return False
                            else:
                                dict[board[3 * i + k][3 * j + h]] = 1

        return True

input = [[".",".","4", ".",".",".", "6","3","."],
         [".",".",".", ".",".",".", ".",".","."],
         ["5",".",".", ".",".",".", ".","9","."],

         [".",".",".", "5","6",".", ".",".","."],
         ["4",".","3", ".",".",".", ".",".","1"],
         [".",".",".", "7",".",".", ".",".","."],

         [".",".",".", "5",".",".", ".",".","."],
         [".",".",".", ".",".",".", ".",".","."],
         [".",".",".", ".",".",".", ".",".","."]]
print(Solution().is_valid_sudoku(input))