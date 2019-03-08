import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        h = []
        for num in nums:
            heapq.heappush(h, num)
        for _ in range(len(nums) - k):
            heapq.heappop(h)
        return heapq.heappop(h)