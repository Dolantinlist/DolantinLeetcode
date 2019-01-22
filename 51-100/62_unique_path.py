class Solution(object):
    def uniquePaths(self, m, n):
        # self.cnt = 0
        # def search_path(x, y):
        #     if x == m and y == n:
        #         self.cnt += 1
        #         return
        #     if x < m :
        #         search_path(x + 1, y)
        #     if y < n:
        #         search_path(x, y + 1)
        #         return
        # search_path(1, 1)
        # return self.cnt
        if m <= 0 or n <= 0:
            return 0
        elif m == 1 or n == 1:
            return 1
        k = [1] * n
        for i in range(1,m):
            for j in range(1,n):
                k[j] += k[j - 1]
        return k[-1]

print(Solution().uniquePaths(7,3))