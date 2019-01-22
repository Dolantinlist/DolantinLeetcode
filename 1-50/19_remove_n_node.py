class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        h, k = head, head
        for i in range(n):
            h = h.next
        if not h:
            return head.next

        while h.next:
            k = k.next
            h = h.next
        k.next = k.next.next

        return head


