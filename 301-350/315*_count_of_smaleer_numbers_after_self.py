class Solution:
    def countSmaller(self, nums):
        rank = {val : k + 1 for k, val in enumerate(sorted(nums))}
        tree = [0] * (len(nums) + 1)
        rlt = []
        def update(x):
            while x <= len(nums):
                tree[x] += 1
                x += x & -x

        def t_sum(x):
            s = 0
            while x:
                s += tree[x]
                x -= x & -x
            return s

        for x in nums[::-1]:
            k = rank[x]
            rlt.append(t_sum(k - 1))
            update(k)

        return rlt[::-1]

print(Solution().countSmaller([5,2,6,1]))
