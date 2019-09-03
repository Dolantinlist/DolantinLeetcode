class Solution:
    def videoStitching(self, clips, T):
        mem = [T + 1] * (T + 1)
        mem[0] = 0
        for i in range(T + 1):
            for c in clips:
                if c[0] <= i and c[1] >= i:
                    mem[i] = min(mem[i], mem[c[0]] + 1)
        return -1 if mem[T] == T + 1 else mem[T]

print(Solution().videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10))