class Solution:
    def getRow(self, rowIndex):
        rlt = [0 for _ in range(rowIndex + 1)]
        rlt[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                rlt[j] += rlt[j - 1]
        return rlt


print(Solution().getRow(3))