class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        k = grid[0]
        for j in range(1, n):
            k[j] += k[j - 1]
        for i in range(1, m):
            for j in range(0, n):
                if j == 0:
                    k[j] += grid[i][j]
                else:
                    k[j] = min(k[j], k[j - 1]) + grid[i][j]
        return k[-1]


input =   [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(Solution().minPathSum(input))
