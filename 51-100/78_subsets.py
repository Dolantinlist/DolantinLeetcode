class Solution(object):
    def subsets(self, nums):
        nums.sort()
        res, tmp = [], []
        self.dfs(nums, 0, tmp, res)
        return res


    def dfs(self, nums, index, tmp, res):
        res.append(tmp)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, tmp + [nums[i]], res)


print(Solution().subsets([1,2,3]))