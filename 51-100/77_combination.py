class Solution(object):
    def combine(self, n, k):
        ans, stack = [], []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:]) #必须加[:]，否则stack更改时ans也会更改
            if l == k or x > n + 1 - (k - l):
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1


print(Solution().combine(5,3))