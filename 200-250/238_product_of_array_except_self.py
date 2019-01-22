class Solution:
    def productExceptSelf(self, nums):
        res = [1]
        for i in range(1, len(nums)):
            res.append(res[i - 1] * nums[i - 1])
        right = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] *= right
            right *= nums[j]
        return res

input = [1, 2, 3, 4]
print(Solution().productExceptSelf(input))