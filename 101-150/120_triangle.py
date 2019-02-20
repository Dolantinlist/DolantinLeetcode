# class Solution:
#     def minimumTotal(self, triangle):
#         l = len(triangle)
#         res = triangle[-1]
#         for i in range(l - 2, -1, -1):
#             for j in range(i + 1):
#                 res[j] = min(res[j], res[j + 1]) + triangle[i][j]
#         return res[0]


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return None
        rlt = [triangle[0]]
        for i in range(1, len(triangle)):
            rlt.append([])
            for j in range(len(triangle[i])):
                if j == 0:
                    rlt[i].append(rlt[i - 1][j] + triangle[i][j])
                elif j == len(triangle[i]) - 1:
                    rlt[i].append(rlt[i - 1][j - 1] + triangle[i][j])
                else:
                     rlt[i].append(min(rlt[i - 1][j - 1], rlt[i - 1][j]) + triangle[i][j])
        return min(rlt[-1])
triangle = [[2], [3,4], [6,5,7],[4,1,8,3]]
print(Solution().minimumTotal(triangle))