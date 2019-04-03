from utils.List import *
class Solution:
    def deleteDuplication(self, pHead : ListNode):
        if not pHead:
            return pHead
        p = ListNode(-1)
        p.next = pHead
        pre = p
        tmp = pHead.val
        cur = pHead.next
        while cur:
            if cur.val != tmp:
                tmp = cur.val
                pre = pre.next
                cur = cur.next
            else:
                while cur and cur.val == tmp:
                    cur = cur.next
                pre.next = cur
                if not cur:
                    break
                tmp = cur.val
                cur = cur.next
        return p.next

ll = creatList([1,2,3,3,4,4,5])
lt = Solution().deleteDuplication(ll)
printList(lt)