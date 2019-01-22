class Solution:
    def minCut(self, s):
        l = len(s)
        nums = [i - 1 for i in range(l + 1)]
        for i in range(l):
            j = 0
            while j <= i and i + j < l and s[i - j] == s[i + j]:
                nums[i + j + 1] = min(nums[i + j + 1], nums[i - j] + 1)
                j += 1
            j = 1
            while j <= i + 1 and i +j <l and s[i - j + 1] == s[i + j]:
                nums[i + j + 1] = min(nums[i + j + 1], nums[i - j + 1] + 1)
                j += 1
        return nums[l]


print(Solution().minCut("bbbabb"))