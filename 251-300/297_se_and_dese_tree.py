from Tree import *
class Codec:
    def serialize(self, root):
        rlt = []
        if not root:
            return rlt
        cur = [root]
        rlt.append(root.val)
        nxt = []
        while cur:
            node = cur.pop(0)
            if node.left:
                rlt.append(node.left.val)
                nxt.append(node.left)
            else:
                rlt.append(None)

            if node.right:
                rlt.append(node.right.val)
                nxt.append(node.right)
            else:
                rlt.append(None)
            if not len(cur):
                cur = nxt
                nxt = []
        while rlt[-1] is None:
            rlt.pop()
        return rlt

    def deserialize(self, nodelist):
        if not nodelist:
            return None
        root = TreeNode(nodelist[0])
        if len(nodelist) == 1:
            return root
        current, curcnt, pre, precnt, i, j = [], 0, [root], 1, 1, 0
        while i < len(nodelist):
            if nodelist[i] == None:
                if j % 2 == 0:
                    pre[j // 2].left = None
                else:
                    pre[j // 2].right = None
            else:
                tmp = TreeNode(nodelist[i])
                current += [tmp]
                curcnt += 1
                if j % 2 == 0:
                    pre[j // 2].left = tmp
                else:
                    pre[j // 2].right = tmp
            i += 1
            j += 1
            if j == 2 * precnt:
                j = 0
                pre, precnt = current, curcnt
                current, curcnt = [], 0
        return root

x = [1,2,3,None, None,4,5]
tree = Codec().deserialize(x)
print(Codec().serialize(tree))