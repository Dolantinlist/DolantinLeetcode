# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head
        cur = head
        nxt = head.next
        while nxt:
            if cur.val == nxt.val:
                cur.next = nxt.next
                nxt = cur.next
            else:
                cur = nxt
                nxt = cur.next

        return head