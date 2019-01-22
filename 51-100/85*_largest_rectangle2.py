class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        h = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in range(n):
                if row[i] == '1':
                    h[i] += 1
                else:
                    h[i] = 0

            stack = [-1]
            for i in range(n + 1): #因为加了一位，别写成n
                while h[i] < h[stack[-1]]:
                    cur = h[stack.pop()]
                    w = i - stack[-1] - 1
                    ans = max(ans, cur * w)
                stack.append(i)
        return ans

iput =[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(Solution().maximalRectangle(iput))