from Tree import *
class Solution:
    def isValidBST(self, root):
        return self.checkBST(root, None, None)
    def checkBST(self, node, minNode, maxNode):
        if not node:
            return True
        elif((minNode and node.val <= minNode.val) or (maxNode and node.val >= maxNode.val)):
            return False
        return self.checkBST(node.left, minNode, node) and self.checkBST(node.right, node, maxNode)

print(Solution().isValidBST(creatTree([5,1,4,None,None,3,6])))