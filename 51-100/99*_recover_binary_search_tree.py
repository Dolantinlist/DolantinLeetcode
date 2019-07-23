from utils.Tree import *
class Solution:
    def recoverTree(self, root):
        res, stack, first, second = None, [], None, None
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            # first time occurs reversed order
            if res and res.val > node.val:
                if not first:
                     first = res
                # first or second time occurs reversed order
                second = node
            res = node
            root = node.right
        first.val, second.val = second.val, first.val
