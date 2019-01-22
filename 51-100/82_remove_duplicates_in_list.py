# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head
        h = ListNode(-1)
        h.next = head
        pre = h
        cur = head
        tmp = head.val
        while cur.next:
            if cur.next.val != tmp:
                pre = cur
                cur = cur.next
            else:
                while cur.next and cur.next.val == tmp:
                    cur = cur.next
                pre.next = cur.next
                cur = pre.next
            if not cur:
                return h.next
            tmp = cur.val
        return h.next



