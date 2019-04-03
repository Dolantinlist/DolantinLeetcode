class Solution(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if not self.stack2:
            while len(self.stack1):
                a = self.stack1.pop()
                self.stack2.append(a)
        return self.stack2.pop()
a = Solution()
a.push(1)
a.push(2)
print(a.pop())