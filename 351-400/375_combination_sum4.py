class Solution(object):
    def combinationSum4(self, nums, target):
        comb = [0] * (target+1)
        nums.sort()
        for i in range(1, target + 1):
            for num in nums:
                if num > i: break
                elif num == i: comb[i] += 1
                else: comb[i] += comb[i - num]
        return comb[target]

print(Solution().combinationSum4([1,2,3], 4))
