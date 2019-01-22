from Tree import *
class Solution:
    def isSymmetric(self, root):
        if not root:
            return  True
        return self.checkSymmetric(root.left, root.right)
    def checkSymmetric(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.checkSymmetric(left.left, right.right) \
            and self.checkSymmetric(left.right, right.left)

print(Solution().isSymmetric(creatTree([1,2,2,None,3,None,3])))