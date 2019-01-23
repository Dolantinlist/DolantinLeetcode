class Solution:
    def largestDivisibleSubset(self, nums):
        l = len(nums)
        if l < 2:
            return nums
        pre = [-1] * l
        cnt = [0] * l
        nums = sorted(nums)
        rlt = []
        for i in range(1, l):
            maxcnt = 0
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if cnt[j] + 1 > maxcnt:
                        pre[i] = j
                        maxcnt = cnt[j] + 1
                        cnt[i] = maxcnt
        index = cnt.index(max(cnt))
        while index >= 0:
            rlt.insert(0, nums[index])
            index = pre[index]
        return rlt

print(Solution().largestDivisibleSubset([]))