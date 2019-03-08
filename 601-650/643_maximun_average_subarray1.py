class Solution:
    def findMaxAverage(self, nums, k):
        rlt = []
        init = sum(nums[:k])
        rlt.append(init)
        for i in range(len(nums) - k):
            init -= nums[i]
            init += nums[i + k]
            rlt.append(init)
        return max(rlt) / k
print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))