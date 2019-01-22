class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        elif len(nums) == 3:
            if sum(nums) == 0:
                return [sorted(nums)]
            else:
                return []
        nums = sorted(nums)
        ans = []

        for i in range(len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                tmp = nums[i] + nums[j] +nums[k]
                if tmp == 0:
                    ans.append((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

                elif tmp > 0:
                    k -= 1
                else:
                    j += 1

        return list(set(tuple(ans)))


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))