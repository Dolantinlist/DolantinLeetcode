class Solution(object):
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        lo, hi = 0, len(nums) - 1
        while(lo < hi):  #这一段真难写
            mid = (lo + hi)//2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        rot = lo
        if nums[-1] >= target:
            lo ,hi = rot, len(nums) - 1
        else:
            lo, hi = 0, rot - 1
        while(lo <= hi):
            mid = (lo + hi)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1


nums = [5,1,3]
target = 5
print(Solution().search(nums,target))
