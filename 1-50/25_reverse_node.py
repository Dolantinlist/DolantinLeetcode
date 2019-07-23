from utils.List import *
def reverseKGroup(head, k):
    dummy = jump = ListNode(0)
    dummy.next = l = r = head

    while True:
        cnt = 0
        while r and cnt < k:
            r = r.next
            cnt += 1
        if cnt != k:
            return dummy.next
        else:
            pre, cur = r, l
            for _ in range(k):
                cur.next, cur, pre = pre, cur.next, cur
            jump.next, jump, l = pre, l, r
