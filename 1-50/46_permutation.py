class Solution(object):
    def permute(self, nums):
        self.res = []
        self.solve(nums, [])
        return self.res

    def solve(self, nums, path):
        if not nums:
            self.res.append(path)
        else:
            for i in range(len(nums)):
                self.solve(nums[:i] + nums[i + 1:], path + [nums[i]])
