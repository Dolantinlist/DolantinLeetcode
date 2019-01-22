class Solution(object):
    def restoreIpAddresses(self, s):
        ans, res = [], []
        self.dfs(s, ans, res, 4)
        return res

    def dfs(self, s, ans, res, k):
        if len(s) > 3*k:
            return
        if k == 0:
            res += ['.'.join(ans)]
        else:
            for i in range(min(3,len(s) - k + 1)):
                #两种例外情况 大于255或者0开头
                if i == 2 and int(s[:3]) > 255 or i > 0 and s[0] == '0':
                    continue
                self.dfs(s[i+1:], ans + [s[:i+1]], res, k - 1)


print(Solution().restoreIpAddresses("25525511135"))