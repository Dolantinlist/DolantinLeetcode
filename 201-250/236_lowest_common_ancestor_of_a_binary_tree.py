from utils import Tree
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        pathp = []
        pathq = []
        self.path_finder(root, pathp, p)
        self.path_finder(root, pathq, q)
        while len(pathp) and len(pathq):
            a = pathp.pop()
            b = pathq.pop()
            if a == b:
                return a
        return -1

    def path_finder(self, node, path, m):
        if not node:
            return False
        path.extend([node.val])
        if node.val == m:
            return True
        if self.path_finder(node.left, path,  m):
            return True
        if self.path_finder(node.right, path, m):
            return True
        path.pop()
        return False

tree = Tree.creatTree([3,5,1,6,2,0,8,None, None,7,4])
print(Solution().lowestCommonAncestor(tree, 5, 1))