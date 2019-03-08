from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        cmpa = lambda a, b: 1 if a+b > b+a else -1 if a+b < b+a else 0
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(cmpa), reverse=True)
        return str(int("".join(nums)))
print(Solution().largestNumber([3,30,34,5,9]))