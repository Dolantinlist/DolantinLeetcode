class Solution:
    def lengthOfLIS(self, nums):
        l = len(nums)
        if l:
            cnt = [1 for _ in range(l)]
            for i in range(1, l):
                maxcnt = 1
                for j in range(0, i):
                    if nums[i] > nums[j]:
                        maxcnt = max(maxcnt, cnt[j] + 1)
                cnt[i] = maxcnt
            return max(cnt)
        return 0

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
