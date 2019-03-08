class Solution:
    def nextGreaterElements(self, nums):
        res = [-1] * len(nums)
        r = list(range(len(nums))) * 2
        stack = []
        for idx in r:
            num = nums[idx]
            while stack and num > nums[stack[-1]]:
                res[stack.pop()] = num
            stack.append(idx)
        return res

print(Solution().nextGreaterElements([1,2,1]))
