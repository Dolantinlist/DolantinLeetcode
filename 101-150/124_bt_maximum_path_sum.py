from Tree import *
class Solution:
    def maxPathSum(self, root):
        self.res = root.val
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return 0
        maxleft = self.helper(root.left)
        maxright = self.helper(root.right)
        tmppath = root.val + maxright + maxleft
        sum = root.val + max(maxleft, maxright, 0)
        self.res = max(self.res, sum, tmppath)
        return sum

root = creatTree([-10,9,20,None,None,15,7])
print(Solution().maxPathSum(root))