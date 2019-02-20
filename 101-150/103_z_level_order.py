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
