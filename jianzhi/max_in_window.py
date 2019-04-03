class Solution:
    def maxInWindows(self, num, size):
        if not size:
            return []
        l = len(num)
        rlt = []
        for i in range(l - size + 1):
            rlt.append(max(num[i:i + size]))
        return rlt

print(Solution().maxInWindows([2,3,4,2,6,2,5,1], 3))
