from Tree import *
class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not left or not right:
            return max(left, right) + 1
        return min(left, right) + 1


tree = creatTree([1,2])
print(Solution().minDepth(tree))
