class Solution:
    def numDecodings(self, s):
        res = [0] * (len(s) + 1)
        res[0] = 1
        for i in range(1, len(s) + 1):
            if s[i - 1] != '0':
                res[i] += res[i - 1]
            #在PEP8中 冒号用作切片时视为二元运算符，两边空格数相等
            #若一侧的参数被省略  则两侧空格都被省略
            if i != 1 and s[i - 2 : i] > '09' and  s[i - 2:] < '27':
                res[i] += res[i - 2]
        return res[len(s)]


print(Solution().numDecodings("226"))