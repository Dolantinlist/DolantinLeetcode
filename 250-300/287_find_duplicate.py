class Solution:
    def findDuplicate(self, nums):
        if not nums:
            return 0
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
input = [1,3,4,2,2]
print(Solution().findDuplicate(input))