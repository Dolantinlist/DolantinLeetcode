class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):
            pre = pre.next

        cur = pre.next
        reverse = None
        for _ in range(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next
        pre.next.next = cur
        pre.next = reverse

        return dummyNode.next

        return dummyNode.next