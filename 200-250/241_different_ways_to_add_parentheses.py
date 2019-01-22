class Solution:
    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]
        res = []
        for i, c in enumerate(input):
            if c in "+-*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for x in res1:
                    for y in res2:
                        res.append(self.helper(c, x, y))
        return res
    def helper(self, op, res1, res2):
        if op == "+":
            return res1 + res2
        elif op == '-':
            return res1 - res2
        else:
            return res1 * res2

input = '2*3-4*5'
print(Solution().diffWaysToCompute(input))