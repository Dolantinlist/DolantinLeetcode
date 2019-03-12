class Solution:
    def search(self, nums, target):
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                h = mid - 1
            else:
                l = mid + 1
        return -1

print(Solution().search([-1,0,3,5,9,12], 9))
