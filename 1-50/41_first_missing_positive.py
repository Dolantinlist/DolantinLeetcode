class Solution(object):
    def first_missing_positive(self, nums):
        nums.append(0)
        for i in range(len(nums)):
            target = nums[i]
            while target < len(nums) and target >= 0 and target != nums[target]:
                tmp = nums[target]
                nums[target] = target
                target = tmp

        for i in range(len(nums)):
            if i != nums[i]:
                return i

        return len(nums)
