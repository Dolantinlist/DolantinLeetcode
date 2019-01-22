from Tree import *
class Solution:
    def levelOrder(self, root):
        queue, nextq, tmp, ans = [], [], [], []
        queue.append(root)
        flag = 0
        while(len(queue)):
            node = queue.pop()
            if not node:
                if len(queue) == 0:
                    flag += 1
                    ans.append(tmp)
                    queue = nextq
                    nextq, tmp = [], []
                continue
            tmp.append(node.val)
            if flag %2 == 0:
                nextq += [node.left, node.right]
            else:
                nextq += [node.right, node.left]
            if len(queue) == 0:
                flag += 1
                ans.append(tmp)
                queue = nextq
                nextq, tmp = [], []

        return ans[:-1]

print(Solution().levelOrder(creatTree([3,9,20,None,None,15,7])))