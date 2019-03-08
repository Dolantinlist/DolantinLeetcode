class Solution:
    def fourSumCount(self, A, B, C, D):
        ab = {}
        for i in A:
            for j in B:
                ab[i+j] = ab.get(i+j, 0) + 1
        rlt = 0
        for i in C:
            for j in D:
                rlt += ab.get(-i-j, 0)
        return rlt