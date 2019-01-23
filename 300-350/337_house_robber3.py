from Tree import *
class Solution:
    def rob(self, root):
        return max(self.helper(root))
    def helper(self, node):
        if not node:
            return [0, 0]  # 0:抢自己, 1:不抢自己, 2:环路
        l = self.helper(node.left)
        r = self.helper(node.right)
        return [l[1] + r[1] + node.val, max(r[0], r[1]) + max(l[0], l[1])]

root = creatTree([3,4,5,1,3,None,1])
print(Solution().rob(root))