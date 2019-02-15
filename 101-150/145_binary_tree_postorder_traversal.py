from Tree import *

#本文件迭代实现了二叉树前序、中序、后序遍历

class Solution:
    def preorderTraversal(self, root):
        rlt = []
        node_stack = []
        p = root
        while node_stack or p:
            if p:
                rlt.append(p.val)
                node_stack.append(p)
                p = p.left
            else:
                node = node_stack.pop()
                p = node.right
        return rlt

    def inorderTraversal(self, root):
        rlt = []
        node_stack = []
        p = root
        while node_stack or p:
            if p:
                node_stack.append(p)
                p = p.left
            else:
                node = node_stack.pop()
                rlt.append(node.val)
                p = node.right
        return rlt

#后序为左右中，实现上可取巧为中右左的反序，实现上类似前序，结果反序即可
#这里选择正常做法
    def postorderTraversal(self, root):
        rlt = []
        node_stack = []
        p = root
        while node_stack or p:
            if p:
                node_stack.append((p, True))
                p = p.left
            else:
                node = node_stack.pop()
                if node[1]:
                    p = node[0].right
                    node_stack.append((node[0], False))
                else:
                    rlt.append(node[0].val)
                    p = None
        return rlt

#以中序为例做一个递归实现
    def recurinorder(self, root):
        rlt = []
        self.recurhelper(root, rlt)
        return rlt

    def recurhelper(self, node, rlt):
        if node:
            self.recurhelper(node.left, rlt)
            rlt.append(node.val)
            self.recurhelper(node.right, rlt)



l = [1, None, 2, 3, 4]
root = creatTree(l)
print(Solution().inorderTraversal(root))