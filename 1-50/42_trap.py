# class Solution(object):
#     def trap(self, height):
#         res, left, right, maxleft, maxright = 0, 0, len(height) - 1, 0, 0
#         while(left < right):
#             if height[left] <= height[right] :
#                 if height[left] >= maxleft:
#                     maxleft = height[left]
#                 else:
#                     res += maxleft - height[left]
#                 left += 1
#             else:
#                 if height[right] >= maxright:
#                     maxright = height[right]
#                 else:
#                     res += maxright - height[right]
#                 right -= 1
#
#         return res
class Solution:
    def trap(self, height):
        if len(height) < 3:
            return 0
        left = [height[0]]
        right = [height[-1]]
        lmax, rmax = height[0], height[-1]
        for i in range(1, len(height)):
            lmax = max(height[i - 1],lmax)
            left.append(lmax)
        for i in range(len(height)-2, -1, -1):
            rmax = max(height[i + 1], rmax)
            right.insert(0, rmax)
        res = 0
        for i in range(len(height)):
            tmp = min(left[i], right[i])
            if tmp > height[i]:
                res += tmp - height[i]
        return res

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))

