class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        res = strs[0]
        l = len(res)
        for i in range (1, len(strs)):
            cp = strs[i]
            j = 0
            while j < min(l, len(cp))and res[j] == cp[j]:
                j += 1
            l = j
        return res[:l]


strs = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strs))