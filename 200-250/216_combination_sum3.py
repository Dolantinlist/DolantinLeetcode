class Solution:
    def combinationSum3(self, k, n):
        res = []
        self.dfs(k, n, 0, [], res)
        return res

    def dfs(self, k, n, index, path, res):
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            res.append(path)
        for i in range(index + 1, 10):
            self.dfs(k - 1, n - i, i,path + [i], res)

k = 3
n = 7
print(Solution().combinationSum3(k,n))