class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None
        if pNode.right:
            p = pNode.right
            while p.left:
                p = p.left
            return p
        while pNode.next:
            p = pNode.next
            if p.left == pNode:
                return p
            pNode = pNode.next
        return None
