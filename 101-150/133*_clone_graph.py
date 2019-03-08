import collections
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        copynode = UndirectedGraphNode(node.label)
        dic = {node: copynode}
        gp = collections.deque([node])
        while gp:
            cur = gp.popleft()
            for n in cur.neighbors:
                if n not in dic:
                    copyneighbor = UndirectedGraphNode(n.label)
                    gp.append(n)
                    dic[n] = copyneighbor
                    dic[cur].neighbors.append(copyneighbor)
                else:
                    dic[cur].neighbors.append(dic[n])
        return dic[node]
