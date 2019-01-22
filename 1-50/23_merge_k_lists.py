from queue import PriorityQueue #优先队列
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def mergeKLists(lists):
    k = len(lists)
    node = head = ListNode(0)
    q = PriorityQueue()
    for n in lists:
        if n:
            q.put((n.val, n))
    while q.qsize() > 0:
        node.next = q.get()[1]
        node = node.next
        if node.next:
            q.put((node.next.val, node.next))
    return head.next


