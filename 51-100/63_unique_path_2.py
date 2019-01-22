class Solution(object):
    def uniquePaths(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m <= 0 or n <= 0 or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        elif m == 1 or n == 1:
                return 1
        k = [1] * n
        for j in range(1,n):
            if obstacleGrid[0][j] == 1:
                k[j:] = [0] * (n - j)
                break
        for i in range(1,m):
            for j in range(0,n):
                if j != 0 and obstacleGrid[i][j] == 0:
                    k[j] += k[j - 1]
                elif j == 0 and obstacleGrid[i][j] == 0:
                    pass
                else:
                    k[j] = 0
        return k[-1]


input = [[0,0],[1,0]]
print(Solution().uniquePaths(input))
