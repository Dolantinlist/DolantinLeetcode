class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
def creatList(nums):
    if len(nums) == 0:
        return None
    tail = None
    while True:
        tmp = ListNode(nums.pop())
        tmp.next = tail
        tail = tmp
        if len(nums) == 0:
            return tmp

def printList(node):
    ans = []
    if not node:
        return ans
    while node:
        ans.append(node.val)
        node = node.next
    print(ans)
