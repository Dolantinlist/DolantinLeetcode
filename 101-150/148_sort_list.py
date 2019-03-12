from utils.List import *
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.mergeList(l, r)

    def mergeList(self, l: ListNode, r: ListNode) -> ListNode:
        if not l or not r:
            return l or r
        if l.val > r.val:
            l, r = r, l
        head = pre = l
        l = l.next
        while l and r:
            if l.val <= r.val:
                l = l.next
            else:
                tmp = r
                r = r.next
                pre.next = tmp
                tmp.next = l
            pre = pre.next
        pre.next = l or r
        return head

l = creatList([-1, 5, 3, 4, 0])
printList(Solution().sortList(l))