class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        l = len(matrix[0])
        j = -1
        for row in matrix:
            while j + l and row[j] > target:
                j -= 1
            if row[j] == target:
                return True
        return False