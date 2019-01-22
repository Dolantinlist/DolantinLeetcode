class Solution:
    def generate(self, numRows):
        rlt = []
        for i in range(numRows):
            tmp = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    tmp.append(1)
                else:
                    tmp.append(rlt[i - 1][j - 1] + rlt[i - 1][j])
            rlt.append(tmp)
        return rlt

print(Solution().generate(5))