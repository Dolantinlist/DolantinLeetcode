class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead or not pHead.next:
            return None
        slow = pHead
        fast = pHead.next
        while fast and fast.next and fast != slow:
            fast = fast.next.next
            slow = slow.next
        if fast != slow:
            return False
        p = fast
        fast = pHead
        while p!=fast:
            p = p.next
            fast = fast.next
        return p
