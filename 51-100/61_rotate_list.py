# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        cnt = 0
        h = ListNode(0)
        h.next = head
        q = p = h
        while q.next != None:
            q = q.next
            cnt += 1
        if cnt != 0:
            k %= cnt
        if k == 0 or cnt == 0:
            return head

        q = h
        for i in range(k):
            q = q.next
        while q.next != None:
            p = p.next
            q = q.next
        q.next = h.next
        h.next = p.next
        p.next = None
        return h.next


