class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        l = len(nums)
        closet = []

        for i, n in enumerate(nums[:-2]):
            j, k = i + 1, l - 1
            if n + nums[k] + nums[k - 1] < target:
                closet.append(n + nums[k] + nums[k - 1])
            elif n + nums[j] + nums[j + 1] >target:
                closet.append(n + nums[j] + nums[j + 1])
            else:
                while j < k:
                    closet.append(n + nums[j] +nums[k])
                    if n + nums[j] +nums[k] > target:
                        k -= 1
                    else:
                        j += 1

        closet.sort(key=lambda x:abs(x-target))
        return  closet[0]