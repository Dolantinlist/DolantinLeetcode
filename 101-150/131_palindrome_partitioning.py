class Solution:
    def partition(self, s):
        res = []
        self.dfshelper(s, [], res)
        return res

    def dfshelper(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            if self.isPal(s[:i]):
                self.dfshelper(s[i:], path + [s[:i]], res)

    def isPal(self, s):
        if s == s[::-1]:
            return True
        return False

test = "aab"
print(Solution().partition(test))