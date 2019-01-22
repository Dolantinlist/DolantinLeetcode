from Tree import *
'''
class Solution:
    def isBalanced(self, root):
        if not root:
            return False

        left = self.depthHelper(root.left)
        right = self.depthHelper(root.right)
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depthHelper(self, root):
        if not root:
            return 0
        return max(root.left, root.right) + 1
'''
class Solution:
    def isBalanced(self, root):
        return self.depthHelper(root) != -1

    def depthHelper(self, root):
        if not root:
            return 0
        left = self.depthHelper(root.left)
        if left == -1:
            return -1
        right = self.depthHelper(root.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return max(left, right) + 1


tree = creatTree([1,2,2,3,3,None,None,4,4])
print(Solution().isBalanced(tree))