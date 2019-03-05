# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1 = l2 = 0
        h1 = headA
        h2 = headB
        while h1:
            l1 += 1
            h1 = h1.next
        while h2:
            l2 += 1
            h2 = h2.next
        if l1 > l2:
            for _ in range(l1 - l2):
                headA = headA.next
        else:
            for _ in range(l2 - l1):
                headB = headB.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA