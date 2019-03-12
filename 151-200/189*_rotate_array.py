class Solution(object):
    def rotate(self, nums, k):
        if not nums:
            return []
        l = len(nums)
        k = k% l
        count = 0
        st = 0
        while count < l:
            p = st + k
            while p%l != st:
                nums[st], nums[p%l] = nums[p%l], nums[st]
                p = p + k
                count += 1
            st += 1
            count += 1
        return nums
print(Solution().rotate([1,2,3,4,5,6,7], 3))
