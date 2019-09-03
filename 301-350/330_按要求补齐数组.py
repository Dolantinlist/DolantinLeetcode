class Solution:
    def minPatches(self, nums, n):
        cnt, idx, miss = 0, 0, 1
        l = len(nums)
        while miss <= n:
            if idx < l and nums[idx] <= miss:
                miss += nums[idx]
                idx += 1
            else:
                cnt += 1
                miss += miss
        return cnt