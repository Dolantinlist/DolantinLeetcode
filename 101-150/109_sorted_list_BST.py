from Tree import *
from List import *
class Solution:
    def sortedListBST(self, head):
        self.node = head
        cnt = 0
        while head:
            cnt += 1
            head = head.next
        return self.inorderHelper(0, cnt - 1)

    def inorderHelper(self, start, end):
        if start > end:
            return None
        mid = start + (end - start)//2
        tmp = TreeNode(0)
        tmp.left = self.inorderHelper(start, mid - 1)
        tmp.val = self.node.val
        self.node = self.node.next
        tmp.right = self.inorderHelper(mid + 1, end)

        return tmp

k = creatList([-10,-3,0,5,9])
tree = Solution().sortedListBST(k)
print(levelOrder(tree))


