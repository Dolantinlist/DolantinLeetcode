from Tree import *
class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            idx = inorder.index(preorder.pop(0))
            root  = TreeNode(inorder[idx])
            root.left = self.buildTree(preorder, inorder[:idx])
            root.right = self.buildTree(preorder, inorder[idx + 1:])
            return root


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
tree = Solution().buildTree(preorder, inorder)
print(levelOrder(tree))