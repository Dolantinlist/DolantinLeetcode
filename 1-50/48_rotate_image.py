class Solution(object):
    def rotate(self, matrix):
        n = len(matrix[0])
        for i in range((n + 1)//2): #同时注意n为单数和双数的情况
            for j in range(n):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n -1 - i][j], matrix[i][j]
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        return matrix #原题要求不返回任何数

input = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
output = Solution().rotate(input)
for i in output:
    print(i)
