from Tree import *
class Solution:
    def hasPathSum(self, root, sum):
    #     self.rlt = []
    #     self.pathHelper(root, sum, [])
    #     return self.rlt
    #
    # def pathHelper(self, root, sum, path):
    #     if not root:
    #         return
    #     if root.val == sum and not root.left and not root.right:
    #         self.rlt.append(path + [root.val])
    #     else:
    #         self.pathHelper(root.left, sum - root.val, path + [root.val])
    #         self.pathHelper(root.right, sum - root.val, path + [root.val])
        res = []
        if root:
            self.dfs(root, sum, [], res)
        return res

    def dfs(self, node, sum, path, res):
        if node.left == None and node.right == None:
            if node.val == sum:
                path += [node.val]
                res.append(path)
            return
        for child in [node.left, node.right]:
            if child:
                self.dfs(child, sum - node.val, path + [node.val], res)


tree = creatTree([5,4,8,11,None,13,4,7,2,None,None,5,1])
print(Solution().hasPathSum(tree,22))