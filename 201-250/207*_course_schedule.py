class Solution:
    def canFinish(self, numCourses, prerequisites):
        l = len(numCourses)
        path = [[] for _ in range(l)]
        visit = [0] * l
        for i in range(len(prerequisites)):
            x, y = prerequisites[i]
            path[y].append(x)

        def check(i):
            if visit[i] == 1:
                return True
            if visit[i] == -1:
                return False
            visit[i] = -1
            for j in path[i]:
                if not check(j):
                    return False
            visit[i] = 1
            return True
        for i in range(l):
            if not check(i):
                return False
        return True

