class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        nums1 = nums[1:]
        nums2 = nums[:-1]
        rlt = [0, 0]
        for j,house in enumerate([nums1, nums2]):
            do = [0] * (len(house) + 1)
            undo = [0] * (len(house) + 1)
            for i in range(1, len(house) + 1):
                do[i] = undo[i - 1] + house[i - 1]
                undo[i] = max(do[i - 1], undo[i - 1])
            rlt[j] = max(do[-1], undo[-1])
        return max(rlt)

print(Solution().rob([1,2,3,1]))