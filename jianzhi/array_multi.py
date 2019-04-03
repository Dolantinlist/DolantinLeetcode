class Solution:
    def multiply(self, A):
        alt = [1] * len(A)
        cur = 1
        for i in range(0, len(A)):
            alt[i] = cur
            cur *= A[i]
        cur = 1
        for i in range(len(A) - 1, -1, -1):
            alt[i] *= cur
            cur *= A[i]
        return alt

print(Solution().multiply([2,3,4]))