class Solution:
    def binaryTreePaths(self, root):
        res  = []
        self.dfs(root, [], res)
        return res

    def dfs(self, node, path, res):
        if not node:
            return
        if not node.left and not node.right:
            res.append("->".join(path + [str(node.val)]))
            return
        self.dfs(node.left, path + [str(node.val)], res)
        self.dfs(node.right, path + [str(node.val)], res)
        return