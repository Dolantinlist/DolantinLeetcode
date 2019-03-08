class Solution:
    def dailyTemperatures(self, T):
        stack = []
        rlt = [0] * len(T)
        for idx in range(len(T)):
            while stack and T[stack[-1]] < T[idx]:
                tmp =stack.pop()
                rlt[tmp] = idx - tmp
            stack.append(idx)
        return rlt

print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
