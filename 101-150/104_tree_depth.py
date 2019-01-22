from Tree import *
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1

print(Solution().maxDepth(creatTree([3,9,20,None,None,15,7])))