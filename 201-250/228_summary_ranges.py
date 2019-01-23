class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []
        i = 0
        res = []
        for j in range(1, len(nums) + 1):
            if j < len(nums):
                if (nums[j] == nums[j - 1] + 1):
                    continue
            if i == j - 1:
                res.append(str(nums[i]))
            else:
                res.append(str(nums[i]) + "->" + str(nums[j - 1]))
            i = j
        return res

nums = [0, 1, 2, 4, 5, 7]
print(Solution().summaryRanges(nums))
