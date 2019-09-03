class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        rows, cols, max_size = len(matrix), len(matrix[0]), 0
        size = [0] * cols
        for i in range(rows):
            count = 0
            for j in range(cols):
                size[j] = size[j] + 1 if matrix[i][j] == '1' else 0
            for j in range(cols):
                if size[j] > max_size:
                    count += 1
                    if count > max_size:
                        max_size += 1
                        break
                else:
                    count = 0
        return max_size*max_size

