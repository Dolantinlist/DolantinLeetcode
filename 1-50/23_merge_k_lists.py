from queue import PriorityQueue #优先队列
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

# def mergeKLists(lists):
#     k = len(lists)
#     node = head = ListNode(0)
#     q = PriorityQueue()
#     for n in lists:
#         if n:
#             q.put((n.val, n))
#     while q.qsize() > 0:
#         node.next = q.get()[1]
#         node = node.next
#         if node.next:
#             q.put((node.next.val, node.next))
#     return head.next

from heapq import heappop, heapreplace, heapify
def mergeKLists(lists):
    dummy = node = ListNode(0)
    h = [(head.val, i, head) for i, head in enumerate(lists) if head]
    heapify(h)
    while h:
        v, i, n = h[0]
        if n.next:
            heapreplace(h, (n.next.val, i, n.next))
        else:
            heappop(h)
        node.next = n
        node = node.next
    return dummy.next