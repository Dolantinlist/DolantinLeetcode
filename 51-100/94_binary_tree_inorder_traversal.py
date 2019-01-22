from Tree import *
class Solution:
    def inorderTraversal(self, root):
        #非递归
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node  = stack.pop()
            res.append(node.val)
            root = node.right


    '''
        #递归
        res = []
        self.inorder(root, res)
        return res
    def inorder(self, root, res):
        if root == None:
            return
        self.inorder(root.left, res)
        res += [root.val]
        self.inorder(root.right, res)
        return
    '''

root = creatTree([1, None, 2, 3])
print(Solution().inorderTraversal(root))

