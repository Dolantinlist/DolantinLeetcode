from Tree import *
class Solution:
    def flatten(self, root):
        prev = None
        self.flatHelper(root, prev)
        root = prev


    def flatHelper(self, root, prev):
        if not root:
            return prev
        prev = self.flatHelper(root.right, prev)
        prev = self.flatHelper(root.left, prev)
        root.right = prev
        root.left = None
        return root
