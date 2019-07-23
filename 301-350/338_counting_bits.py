class Solution:
    def countBits(self, num: int):
        cnt = [0] * (num + 1)
        for i in range(1, num + 1):
            p = i&(i-1)
            cnt[i] = cnt[p] + 1
        return cnt

print(Solution().countBits(5))