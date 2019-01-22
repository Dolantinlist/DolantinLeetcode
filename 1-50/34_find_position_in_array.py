class Solution(object):
    def search_range(self, nums, target):
        start, end = -1, -1
        for i in range(len(nums)):
            if nums[i] == target:
                if start == -1:
                    start = i
                    end = i
                else:
                    end = i
        return [start, end]


nums = [5,7,7,8,8,10]
target = 6
rlt = Solution().search_range(nums,target)
for i in rlt:
    print(i)