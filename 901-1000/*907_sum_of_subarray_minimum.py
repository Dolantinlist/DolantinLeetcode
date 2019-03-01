class Solution:
    def sumSubarrayMins(self, A):
        l_idx = list(range(len(A), 0, -1))
        r_idx = list(range(len(A), 0, -1))

        l_stack = []
        r_stack = []
        for idx in range(len(A)):
            while r_stack  and A[r_stack[-1]] > A[idx]:
                tmp = r_stack.pop()
                r_idx[tmp] = idx - tmp
            r_stack.append(idx)

        r_A = A[::-1]
        for idx in range(len(A)):
            while l_stack and r_A[l_stack[-1]] >= r_A[idx]:
                tmp = l_stack.pop()
                l_idx[tmp] = idx - tmp
            l_stack.append(idx)
        l_idx.reverse()

        rlt = 0
        for idx in range(len(A)):
            rlt += r_idx[idx] * l_idx[idx] * A[idx]

        return rlt % (10**9 + 7)

print(Solution().sumSubarrayMins([71,55,82,55]))

'''
左寻
    def sumSubarrayMins(self, A):
        n, mod = len(A), 10**9 + 7
        left, right, s1, s2 = [0] * n, [0] * n, [], []
        for i in range(n):
            count = 1
            while s1 and s1[-1][0] > A[i]: count += s1.pop()[1]
            left[i] = count
            s1.append([A[i], count])
        for i in range(n)[::-1]:
            count = 1
            while s2 and s2[-1][0] >= A[i]: count += s2.pop()[1]
            right[i] = count
            s2.append([A[i], count])
        return sum(a * l * r for a, l, r in zip(A, left, right)) % mod


'''