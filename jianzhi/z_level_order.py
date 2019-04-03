from utils.Tree import *
class Solution:
    def levelOrder(self, root):
        queue, nextq, ans = [], [], []
        queue.append(root)
        flag = 0
        while True:
            node = queue.pop(0)
            ans.append(node.val)
            tmp = []
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
            if flag%2 == 0:
                nextq += tmp
            else:
                nextq += tmp[::-1]
            if len(queue) == 0:
                if len(nextq) == 0:
                    break
                else:
                    queue = nextq[::-1]
                    nextq = []
                    flag += 1
        return ans

print(Solution().levelOrder(creatTree([8,6,10,5,7,9,11])))