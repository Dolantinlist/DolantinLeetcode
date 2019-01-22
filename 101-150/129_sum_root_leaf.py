from Tree import *
class Solution:
    def sumNumber(self, root):
        if not root:
            return 0
        stack, res = [(root, root.val)], 0
        while stack:
            node, value = stack.pop()
            if not node.left and not node.right:
                res += value
            else:
                if node.right:
                    stack.append((node.right, 10*value + node.right.val))
                if node.left:
                    stack.append((node.left, 10*value + node.left.val))
        return res


tree = creatTree([4,9,0,5,1])
print(Solution().sumNumber(tree))
