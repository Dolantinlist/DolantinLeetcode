class Solution(object):
    def spiralOrder(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    res += [row.pop()]
            if matrix:
                res += matrix.pop(-1)[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res += [row.pop(0)]
        return res


print(Solution().spiralOrder([[7],[9],[6]]))