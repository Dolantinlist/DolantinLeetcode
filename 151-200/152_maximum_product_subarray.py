class Solution(object):
    def maxProdcut(self, nums):
        if not len(nums):
            return None
        tmp = imax = imin = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])

            tmp = max(imax, tmp)
        return tmp

nums = [2,3,-2,4]
print(Solution().maxProdcut(nums))