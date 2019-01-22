class Solution:
    def numDistinct(self, s, t):
        l1 = len(s)
        l2 = len(t)
        tmp = [[0 for _ in range(l1 + 1)] for _ in range(l2 + 1)]
        for i in range(l1 + 1):
            tmp[0][i] = 1
        for i in range(1, l2 + 1):
            for j in range(1, l1 + 1):
                tmp[i][j] = tmp[i][j - 1]
                if s[j - 1] == t[i - 1]:
                    tmp[i][j] += tmp[i - 1][j - 1]
        return tmp[l2][l1]


s = "babgbag"
t =  "bag"
print(Solution().numDistinct(s,t))