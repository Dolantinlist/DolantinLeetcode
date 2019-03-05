class Solution:
    def findOrder(self, numCourses, prerequisites):
        visit = [0] * numCourses
        precourse = [[] for _ in range(numCourses)]
        rlt = []
        for pair in prerequisites:
            precourse[pair[0]].append(pair[1])
        for i in range(numCourses):
            if len(precourse[i]) == 0:
                visit[i] = 1
                rlt.append(i)
        def check_course(i):
            if visit[i] == 1:
                return True
            if visit[i] == -1:
                return False
            visit[i] = -1
            for j in precourse[i]:
                if not check_course(j):
                    return False
            visit[i] = 1
            rlt.append(i)
            return True
        for i in range(numCourses):
            if not check_course(i):
                return []
        return rlt
print(Solution().findOrder(3, [[0,1], [0,2], [1,2]]))