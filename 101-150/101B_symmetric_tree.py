from Tree import *
class Solution:
    def isSymmetric(self,root):
        if not root:
            return True
        stack=[[root.left,root.right]]
        while(len(stack) > 0):
            pair = stack.pop()
            left,right = pair[0],pair[1]
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            stack.append([left.left,right.right])
            stack.append([left.right,right.left])

        return True

print(Solution().isSymmetric(creatTree([1,2,2,None,3,None,3])))