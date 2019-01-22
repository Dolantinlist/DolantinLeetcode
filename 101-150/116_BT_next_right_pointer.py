from Tree import *
class Solution:
    def connect(self, root):
        if not root:
            return
        while root.left:
            cur = root.left
            prev = None
            while root:
                if prev:
                    prev.next = root.left
                root.left.next = root.right
                prev = root.right
                root = root.next
            root = cur