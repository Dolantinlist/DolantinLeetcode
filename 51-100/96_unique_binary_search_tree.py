class Solution:
    def numTrees(self, n):
        nums = [0] * (n + 1)
        nums[0], nums[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                nums[i] += nums[j - 1] * nums[i - j]
        return nums[-1]

print(Solution().numTrees(3))