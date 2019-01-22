class Solution(object):
    def generateMatrix(self, n):
        i, j, di, dj = 0, 0, 0, 1
        nums = []
        for _ in range(n):
            nums.append([0] * n)
        for k in range(n*n):
            nums[i][j] = k + 1
            if nums[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di
            i += di
            j += dj
        return nums


print(Solution().generateMatrix(4))