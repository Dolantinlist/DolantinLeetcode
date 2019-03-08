class Solution:
    def canCompleteCircuit(self, gas, cost):
        start, res, overall = 0, 0, 0
        for i in range(len(gas)):
            res += gas[i] - cost[i]
            overall += gas[i] - cost[i]
            if res < 0:
                res, start = 0, i+1
        return start if overall>=0 else -1
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(Solution().canCompleteCircuit(gas, cost))