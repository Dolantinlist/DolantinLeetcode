class Solution(object):
    def solveNQueens(self, n):
        res = []
        rlt = []
        if not n:
            return None
        self.dfs(n, [], [], [], res)
        for ans in res:
            tmp = []
            for j in ans:
                tmp += ["." * j + "Q" + "." * (n - 1 - j)]
            rlt.append(tmp)
        return rlt
    def dfs(self, n, queen, add, diff, res):
        i = len(queen)
        if i == n:
            res.append(queen)
            return
        for j in range(n):
            if j not in queen and i + j not in add and i - j not in diff:
                self.dfs(n, queen + [j], add + [i + j], diff + [i - j], res)

    # def solveNQueens(self, n):
    #     self.n = n
    #     self.res = []
    #     rlt = []
    #     self.dfs([],[],[])
    #     for i in self.res:
    #         tmp = []
    #         for j in i:
    #             tmp += ["." * j + "Q" + "." * (n - 1 - j)]
    #         rlt.append(tmp)
    #     return rlt
    #
    # def dfs(self, queen, add, diff):
    #     i = len(queen)
    #     if len(queen) == self.n:
    #         self.res.append(queen)
    #         return
    #     else:
    #         for j in range(self.n):
    #             if j not in queen and i + j not in add and i - j not in diff:
    #                 self.dfs(queen + [j], add + [i + j], diff + [i - j])


print(Solution().solveNQueens(4))