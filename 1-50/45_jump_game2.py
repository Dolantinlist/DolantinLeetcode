class Solution(object):
    def jump2(self, A):
        ans = lastIdx = nextIdx = 0
        while nextIdx < len(A) - 1:
            ans += 1
            lastIdx, nextIdx = nextIdx, max(i + A[i] for i in range(lastIdx, nextIdx + 1))
        return ans
input = [1,3,2,4,3,4]
#input = [6,2,6,1,7,9,3,5,3,7,2,8,9,4,7,7,2,2,8,4,6,6,1,3]
print(Solution().jump2(input))
'''
    def jump_game(self, nums):
        self.nums = nums
        self.res = target = len(nums) - 1
        self.solve(0, [], target)
        return self.res

    def solve(self, start, path, target):
        if start > len(self.nums) - 1:
            return
        elif target == 0:
            tmp = len(path)
            if tmp < self.res:
                self.res = tmp
            return
        elif target < 0:
            return
        else:
            if self.nums[start] == 0:
                return
            for i in range(1, self.nums[start] + 1):
                self.solve(start + i, path + [i], target - i)
'''

