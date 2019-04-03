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

print(Solution().levelOrder(creatTree([3,9,20,None,None,15,7])))
'''
new code
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [root]
        rlt = [[root.val]]
        cnt = 1
        while stack:
            new_stack = []
            cur_rlt = []
            for node in stack:
                if node.left:
                    new_stack.append(node.left)
                    cur_rlt.append(node.left.val)
                if node.right:
                    new_stack.append(node.right)
                    cur_rlt.append(node.right.val)
            
            if cnt%2:
                cur_rlt.reverse()
            if cur_rlt:
                rlt.append(cur_rlt)
            stack = new_stack
            cnt +=1
        return rlt
'''
