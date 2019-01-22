class Solution(object):
    def search_inseart(self, nums, target):
        if len(nums) == 0:
            return -1
        elif nums[0] > target:
            return 0
        elif nums[-1] < target:
            return len(nums)
        else:
            lo , hi = 0, len(nums) - 1
            while(lo <= hi):
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return lo