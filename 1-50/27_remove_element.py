class Solution(object):
    def removeElement(self, nums, val):
        l =len(nums)
        if l == 0:
            return 0
        else:
            k = 0
            for i in range(l):
                if nums[i] != val:
                    nums[k] = nums[i]
                    k += 1
        return k