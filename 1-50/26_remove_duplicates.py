class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        else:
            k = 0
            for i in range(1, l):
                if nums[i] != nums[k]:
                    k += 1
                    nums[k] = nums[i]

        return k + 1