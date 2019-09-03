class Solution:
    def __init__(self):
        self.mem = [0] * 10001

    def racecar(self, target):
        if self.mem[target] > 0:
            return self.mem[target]
        tmp = 1
        while 2**tmp - 1 <= target:
            tmp += 1

        if 2**(tmp - 1) - 1 == target:
            self.mem[target] = tmp - 1
        else:
            self.mem[target] = tmp + 1 + self.racecar(2**tmp - 1 - target)
            for i in range(0, tmp):
                self.mem[target] = min(self.mem[target], i + tmp + 1 + self.racecar(target + 2**i - 2**(tmp -1)))
        return self.mem[target]

print(Solution().racecar(6))
