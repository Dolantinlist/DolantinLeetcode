from utils.List import *
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        evenhead =  even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        odd.next = evenhead
        return head

l = creatList([1,2,3,4,5,6])
printList(Solution().oddEvenList(l))
