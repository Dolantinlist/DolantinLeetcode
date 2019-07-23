from utils.Tree import *
class Solution:
    def preorderTracersal(self, root: TreeNode):
        stack, res = [], []
        while True:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            if len(stack) == 0:
                return res
            node = stack.pop()
            root = node.right


t = creatTree([1, None, 2, 3])
print(Solution().preorderTracersal(t))
