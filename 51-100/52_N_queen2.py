class Solution(object):
    def totalNQueens(self, n):
        self.n = n
        self.res = []
        self.dfs([], [], [])
    
        return len(self.res)


    def dfs(self, queen, add, diff):
        i = len(queen)
        if len(queen) == self.n:
            self.res.append(queen)
            return
        else:
            for j in range(self.n):
                if j not in queen and i + j not in add and i - j not in diff:
                    self.dfs(queen + [j], add + [i + j], diff + [i - j])