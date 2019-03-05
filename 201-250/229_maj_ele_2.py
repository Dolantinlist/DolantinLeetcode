class Solution:
    def majorityElement(self, nums):
        if not nums:
            return []
        r1 = [0, 0]
        r2 = [1, 0]
        for num in nums:
            if num == r1[0]:
                r1[1] += 1
            elif num == r2[0]:
                r2[1] += 1
            elif r1[1] <= 0:
                r1 = [num, 1]
            elif r2[1] <= 0:
                r2 = [num, 1]
            else:
                r1[1] -= 1
                r2[1] -= 1
        rlt = []
        if nums.count(r1[0]) > len(nums)//3:
            rlt.append(r1[0])
        if nums.count(r2[0]) > len(nums)//3:
            rlt.append(r2[0])
        return rlt

print(Solution().majorityElement([1,1,1,3,3,2,2,2]))

