class Solution(object):
    def nextPermutation(self, nums):
        l = len(nums) - 1
        j = -1
        for i in range(l, -1, -1):
            if nums[i-1] < nums[i]:
                j = i - 1
                break

        for i in range(l, -1, -1):
            if nums[i] > nums[j]:
                nums[j], nums[i] = nums[i], nums[j]
                nums[j+1:] = sorted(nums[j+1:])
                return