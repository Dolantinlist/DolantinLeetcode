class Solution(object):
    def canJump(self, nums):

        def solve(startid, nextid):
            if nextid >= len(nums) - 1:
                return True
            max = 0
            for i in range(startid, nextid + 1):
                tmp = i + nums[i]
                if tmp > max:
                    max = tmp
            if max == nextid:
                return False
            return solve(nextid, max)

        return solve(0,0)

print(Solution().canJump([3,2,1,0,4]))