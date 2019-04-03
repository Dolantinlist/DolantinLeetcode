class Solution:
    def movingCount(self, threshold, rows, cols):
        mark = [[0] * cols for _ in range(rows)]
        return self.check(mark, rows, cols, 0, 0, threshold)

    def check(self, mark, rows, cols, i, j, threshold):
        if i < 0 or i> rows - 1 or j < 0 or j > cols - 1 or mark[i][j] == 1 or self.numsum(i) + self.numsum(j) > threshold:
            return 0
        mark[i][j] = 1
        return self.check(mark, rows, cols, i + 1, j, threshold) + \
               self.check(mark, rows, cols, i - 1, j, threshold) + \
               self.check(mark, rows, cols, i, j + 1, threshold) + \
               self.check(mark, rows, cols, i, j - 1, threshold) +  1

    def numsum(self, num):
        rlt = 0
        while num:
            rlt += num%10
            num = int(num/10)
        return rlt

print(Solution().movingCount(5, 10, 10))