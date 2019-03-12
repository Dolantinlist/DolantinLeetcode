# class Solution(object):
#     def searchMatrix(self, matrix, target):
#         m = len(matrix)
#         if m == 0:
#             return False
#         else:
#             n = len(matrix[0])
#             if  n == 0:
#                 return False
#         l, r = 0, m * n - 1
#         while l <= r:
#             mid = (l + r) // 2
#             num = matrix[mid // n][mid % n]
#
#             if num == target:
#                 return True
#             elif num > target:
#                 r -= 1
#             else:
#                 l += 1
#         return False
class Solution(object):
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        l, h = 0, m*n - 1
        while l <= h:
            mid  = (l + h) // 2
            num = matrix[mid//n][mid%n]
            if num == target:
                return True
            if num > target:
                h = mid - 1
            else:
                l = mid + 1
        return False