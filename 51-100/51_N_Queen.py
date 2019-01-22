class Solution(object):
    def solveNQueens(self, n):
        self.n = n
        self.res = []
        rlt = []
        self.dfs([],[],[])
        for i in self.res:
            tmp = []
            for j in i:
                tmp += ["." * j + "Q" + "." * (n - 1 - j)]
            rlt.append(tmp)
        return rlt

    def dfs(self, queen, add, diff):
        i = len(queen)
        if len(queen) == self.n:
            self.res.append(queen)
            return
        else:
            for j in range(self.n):
                if j not in queen and i + j not in add and i - j not in diff:
                    self.dfs(queen + [j], add + [i + j], diff + [i - j])


print(Solution().solveNQueens(4))