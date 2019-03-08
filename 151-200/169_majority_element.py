class Solution(object):
    def majorityElement(self, nums):
        if not nums:
            return 0
        cnt = [nums[0], 0]
        for num in nums:
            if num == cnt[0]:
                cnt[1] += 1
            else:
                if cnt[1] == 0:
                    cnt = [num, 1]
                else:
                    cnt[1] -= 1
        return cnt[0]


print(Solution().majorityElement([2,2,1,1,1,2,2]))