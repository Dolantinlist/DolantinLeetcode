class Solution(object):
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        elif len(nums) == 4 and sum(nums) == target:
            return [sorted(nums)]

        res = []
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(len(nums) - 1, i + 2, -1):
                if j < len(nums) - 1 and nums[j] == nums[j + 1]:
                    continue
                k, l = i + 1, j - 1
                goal = target - nums[i] - nums[j]
                if nums[k] + nums[k + 1] > goal:
                    continue
                elif nums[l] + nums[l - 1] < goal:
                    continue
                else:
                    while k < l:
                        if k > i + 1 and nums[k] == nums[k - 1]:
                            k += 1
                            continue
                        elif l < j - 1 and nums[l] == nums[l + 1]:
                            l -= 1
                            continue
                        else:
                            if nums[k] + nums[l] == goal:
                                res.append((nums[i], nums[k], nums[l], nums[j]))
                                l -= 1
                                k += 1
                            elif nums[k] + nums[l] > goal:
                                l -= 1
                            else:
                                k += 1

        return res

nums = [0, 0, 0, 0]
print(Solution().fourSum(nums, 0))

