from Tree import *
class Solution:
    def levelOrderBottom(self, root):
        queue, nextq, tmp, ans = [], [], [], []
        queue.append(root)
        while(len(queue)):
            node = queue.pop(0)
            if not node:
                if len(queue) == 0:
                    ans.append(tmp)
                    queue = nextq
                    nextq, tmp = [], []
                continue
            tmp.append(node.val)
            nextq.append(node.left)
            nextq.append(node.right)
            if len(queue) == 0:
                ans.append(tmp)
                queue = nextq
                nextq, tmp = [], []
        return ans[:-1][::-1]

print(Solution().levelOrderBottom(creatTree([3,9,20,None,None,15,7])))