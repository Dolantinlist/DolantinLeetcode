class Solution:
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        i = sums = 0
        res = len(nums) + 1
        for j in range(len(nums)):
            sums += nums[j]
            while sums >= s:
                res = min(res, j - i + 1)
                sums -= nums[i]
                i += 1
        return res if res <= len(nums) else 0