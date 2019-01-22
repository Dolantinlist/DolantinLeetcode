class Solution:
    def singleNumber(self, nums):
        rlt = 0
        for num in nums:
            rlt ^= num
        return rlt