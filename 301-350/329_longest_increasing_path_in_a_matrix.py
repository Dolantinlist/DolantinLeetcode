class Solution:
    def longestIncreasingPath(self, matrix):
        def dfs(i, j):
            if not dp[i][j]:  #important
                val =  matrix[i][j]
                dp[i][j] = max([
                    dfs(i - 1, j) if i > 0 and val > matrix[i -1][j] else 0,
                    dfs(i, j - 1) if j > 0 and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < n - 1 and val > matrix[i][j + 1] else 0,
                    dfs(i + 1, j) if i < m - 1 and val > matrix[i + 1][j] else 0
                ]) + 1
            return dp[i][j]
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        return max([dfs(i, j) for i in range(m) for j in range(n)])

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
print(Solution().longestIncreasingPath(nums))


