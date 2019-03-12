class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lens, lenp = len(s), len(p)
        matrix = [[False] * (lenp + 1) for _ in range(lens + 1)]
        matrix[0][0] = True
        for i in range(2, lenp + 1):
            matrix[0][i] = matrix[0][i - 2] and p[i - 1] == '*'
        for i in range(1, lens + 1):
            for j in range(1, lenp + 1):
                if p[j - 1] == '*':
                    matrix[i][j] = matrix[i][j - 2] or matrix[i][j - 1]
                    if p[j - 2] in ['.', s[i - 1]]:
                        matrix[i][j] |= matrix[i - 1][j]
                else:
                    matrix[i][j] = matrix[i - 1][j - 1] and p[j - 1] in ['.', s[i - 1]]
        return matrix[-1][-1]

print(Solution().isMatch('aab', 'c*a*b'))