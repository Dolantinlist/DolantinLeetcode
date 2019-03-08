import collections
class Solution(object):
    def findItinerary(self, tickets):
        graph = collections.defaultdict(list)
        for t in tickets:
            graph[t[0]].append(t[1])
        for t in graph:
            graph[t].sort(reverse=True)
        path = []
        self.dfs(graph, 'JFK', path, len(tickets) + 1)
        return path

    def dfs(self, graph, start, path, l):
        path.append(start)
        if len(path) == l:
            return True
        if start in graph:
            lnum = len(graph[start])
            i = 0
            while i < lnum:
                tmp = graph[start].pop()
                if self.dfs(graph, tmp, path, l):
                    return True
                graph[start].insert(0, tmp)
                i += 1
        path.pop()
        return False

print(Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))