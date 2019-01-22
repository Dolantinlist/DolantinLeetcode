class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
def levelOrder(root):
    queue, nextq, tmp, ans = [], [], [], []
    queue.append(root)
    while(len(queue)):
        node = queue.pop(0)
        if not node:
            tmp.append(None)
            if len(queue) == 0:
                ans.extend(tmp)
                queue = nextq
                nextq, tmp = [], []
            continue
        tmp.append(node.val)
        nextq.append(node.left)
        nextq.append(node.right)
        if len(queue) == 0:
            ans.extend(tmp)
            queue = nextq
            nextq, tmp = [], []
    return ans[:-1]

def creatTree(nodelist):
    if not nodelist:
        return None
    root = TreeNode(nodelist[0])
    if len(nodelist) == 1:
        return root
    current, curcnt, pre, precnt, i, j =[], 0, [root], 1, 1, 0
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

