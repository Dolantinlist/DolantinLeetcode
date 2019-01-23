class  Solution:
    def rob(self, nums):
        do = [0] * (len(nums) + 1)
        undo = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            do[i] = undo[i - 1] + nums[i - 1]
            undo[i] = max(do[i - 1], undo[i - 1])
        return max(do[-1], undo[-1])
print(Solution().rob([2,1,1,2]))