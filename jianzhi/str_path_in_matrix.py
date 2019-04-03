class Solution:
    def hasPath(self, matrix, rows, cols, path):
        mark = [[False] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if self.helper(matrix, path, mark, i, j, rows, cols, 0):
                    return True
        return False

    def helper(self, matrix, path, mark, i, j, rows, cols, k):
        if i < 0 or i > rows - 1 or j < 0  or j > cols - 1 or matrix[i][j] != path[k] or mark[i][j] == True:
            return False
        mark[i][j] = True
        if k == len(path) - 1:
            return True
        if self.helper(matrix, path, mark, i - 1, j, rows, cols, k + 1) or \
            self.helper(matrix, path, mark, i + 1, j, rows, cols, k + 1) or \
            self.helper(matrix, path, mark, i, j - 1, rows, cols, k + 1) or \
            self.helper(matrix, path, mark, i, j + 1, rows, cols, k + 1) :
            return True
        mark[i][j] = False
        return False
