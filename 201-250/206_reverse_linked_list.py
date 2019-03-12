from utils.List import *
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = head
        q = head.next
        p.next = None
        while q:
            r = q.next
            q.next = p
            p = q
            q = r
        return p
l = creatList([1,2,3,4,5])
printList(Solution().reverseList(l))
