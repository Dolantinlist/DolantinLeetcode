from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        dic = Counter(nums)
        rlt = heapq.nlargest(k, dic, key=lambda x: dic.get(x))
        return rlt

Solution().topKFrequent([1,1,2,3,4,3], 2)