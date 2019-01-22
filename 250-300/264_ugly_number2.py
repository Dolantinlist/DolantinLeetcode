# class Solution:
#     def nthUglyNumber(self, n):
#         res = [1]
#         i2, i3, i5 = 0, 0, 0
#         while n > 1:
#             u2, u3, u5 = res[i2] * 2, res[i3] * 3, res[i5] * 5
#             umin = min(u2, u3, u5)
#             res.append(umin)
#             n -= 1
#             if umin == u2:
#                 i2 += 1
#             if umin == u3:
#                 i3 += 1
#             if umin == u5:
#                 i5 += 1
#         return res[-1]
#
# print(Solution().nthUglyNumber(10))
import heapq
class Solution:
    def nthUglyNumber(self, n):
        tmp = [1]
        res = []
        while n:
            item = heapq.heappop(tmp)
            if item not in res:
                res.append(item)
                n -= 1
                for i in [item*2, item*3, item*5]:
                    heapq.heappush(tmp, i)
        return res[-1]

print(Solution().nthUglyNumber(10))