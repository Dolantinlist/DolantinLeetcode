from utils.List import *
class Solution:
    def isPalindrome(self, head : ListNode) -> bool:
        if not head or not head.next:
            return True
        cnt = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            cnt += 1

        h = head
        for _ in range(cnt//2):
            h = h.next
        p = h.next
        h.next = None
        while p:
            r = p.next
            p.next = h
            h = p
            p = r
        while h and head:
            if h.val != head.val:
                return False
            h = h.next
            head = head.next
        return True

l = creatList([1,2, 3, 4, 2,1])
print(Solution().isPalindrome(l))

