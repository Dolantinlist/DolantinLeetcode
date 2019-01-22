from Tree import *
class Solution(object):
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.dfs(1, n + 1)

    def dfs(self, start, end):
        result = []
        if start == end:
            result.append(None)
        for i in range(start, end):
            for l in self.dfs(start, i):
                for r in self.dfs(i + 1, end):
                    node = TreeNode(i)
                    node.left, node.right = l, r
                    result.append(node)
        return result
root = Solution().generateTrees(3)
print(list(map(levelOrder, root)))