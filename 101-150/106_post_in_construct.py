from Tree import *
class Solution:
    def buildTree(self, inorder, postorder):
        if inorder:
            idx = inorder.index(postorder.pop(-1))
            root  = TreeNode(inorder[idx])
            root.right = self.buildTree(inorder[idx + 1:], postorder)
            root.left = self.buildTree(inorder[:idx],postorder)
            return root


inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
tree = Solution().buildTree(inorder, postorder)
print(levelOrder(tree))