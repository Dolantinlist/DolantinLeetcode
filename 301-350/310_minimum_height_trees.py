class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]
        adj = [set() for _ in range(n)]
        for edge in edges:
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        while n > 2:
            n -= len(leaves)
            newleaves = []
            for k in leaves:
                j = adj[k].pop()
                adj[j].remove(k)
                if len(adj[j]) == 1:
                    newleaves.append(j)
            leaves = newleaves
        return leaves