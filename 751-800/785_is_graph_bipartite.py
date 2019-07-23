class Solution:
    def isBipartite(self, graph):
        group = {}
        def dfs(x, g):
            if x in group:
                return g == group[x]
            group[x] = g
            return all(dfs(y, 1-g) for y in graph[x])
        return all(dfs(x, 0) for x in range(len(graph)) if x not in group)


print(Solution().isBipartite([[1,3],[0,2],[1,3],[0,2]]))