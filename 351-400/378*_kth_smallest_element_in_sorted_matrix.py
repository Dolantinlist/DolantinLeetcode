import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        if not matrix:
            return None
        m = len(matrix)
        l = len(matrix[0])
        h = [(matrix[0][i], 0, i) for i in range(l)]
        heapq.heapify(h)
        i = 0
        while i < k:
            s = heapq.heappop(h)
            i += 1
            if i == k:
                return s[0]
            if s[1] < m - 1:
                heapq.heappush(h, (matrix[s[1] + 1][s[2]], s[1] + 1, s[2]))

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
print(Solution().kthSmallest(matrix, k))
