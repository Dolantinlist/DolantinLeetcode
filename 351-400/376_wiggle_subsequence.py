class Solution:
    def wiggleMaxLength(self, nums):
        l = len(nums)
        if not l:
            return 0
        up = [1] * l
        down = [1] * l
        for i in range(1, l):
            if nums[i] > nums[i - 1]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                down[i] = up[i - 1] + 1
                up[i] = up[i - 1]
            else:
                down[i] = down[i - 1]
                up[i] = up[i - 1]
        return max(up[-1], down[-1])
print(Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
