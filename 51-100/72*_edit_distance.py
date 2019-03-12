class Solution:
    def minDistance(self, word1, word2):
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        m = len(word1)
        n = len(word2)
        INF = float("inf")
        matrix = [[INF for _ in range(n+1)] for _ in range(m+1)]
        for i in range(n):
            matrix[0][i] = i
        for i in range(m):
            matrix[i][0] = i
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    matrix[i][j] = min(matrix[i - 1][j - 1], 1 + matrix[i -1][j], 1 + matrix[i][j - 1])
                else:
                    matrix[i][j] = 1 + min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1])
        return matrix[-1][-1]

print(Solution().minDistance("intention", "execution"))