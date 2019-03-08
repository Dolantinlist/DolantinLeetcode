import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counters = collections.Counter(nums1)
        rlt = []
        for n in nums2:
            if counters[n] > 0:
                rlt.append(n)
                counters[n] -= 1
        return rlt