from List import  *
class Solution:
    def insertionSortList(self, head):
        if head == None:
            return head
        helper = ListNode(0)
        helper.next = head
        cur, tmp, pre, next = head.next, head, helper, None
        while(cur):
            next = cur.next
            while(pre.next and pre.next.val < cur.val):
                pre = pre.next
            if pre.next == cur:
                tmp = cur
                cur = next
                pre = helper
            else:
                cur.next = pre.next
                pre.next = cur
                tmp.next = next
                tmp = helper
                while(tmp.next != next):
                    tmp = tmp.next
                cur = next
                pre = helper
            printList(helper.next)
        return helper.next

l = creatList([-1,5,3,4,0])
printList(Solution().insertionSortList(l))
