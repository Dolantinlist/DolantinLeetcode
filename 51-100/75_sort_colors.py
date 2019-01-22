class Solution(object):
    def sortColors(self, nums):
        i, j = 0, 0
        for k in range(len(nums)):
            n = nums[k]
            nums[k] = 2
            if n < 2:
                nums[j] = 1
                j += 1
            if n == 0:
                nums[i] = 0
                i += 1

        return nums

print(Solution().sortColors([2,0,1,1]))
