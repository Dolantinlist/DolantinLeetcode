class Solution:
    def intToRoman(self, num):
        M = ['', 'M', 'MM', 'MMM']
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        return M[int(num / 1000)] + C[int((num % 1000) / 100)] + X[int((num % 100) / 10)] + I[num % 10]

    # 能把代码写这么笨拙 我也是相当蠢了
    # res = ''
    # while num >= 1000:
    #     num -= 1000
    #     res += 'M'
    # while num >= 900:
    #     num -= 900
    #     res += 'CM'
    # while num >= 500:
    #     num -= 500
    #     res += 'D'
    # while num >= 400:
    #     num -= 400
    #     res += 'CD'
    # while num >= 100:
    #     num -= 100
    #     res += 'C'
    # while num >= 90:
    #     num -= 90
    #     res += 'XC'
    # while num >= 50:
    #     num -= 50
    #     res += 'L'
    # while num >= 40:
    #     num -= 40
    #     res += 'XL'
    # while num >= 10:
    #     num -= 10
    #     res += 'X'
    # while num >= 9:
    #     num -= 9
    #     res += 'IX'
    # while num >= 5:
    #     num -= 5
    #     res += 'V'
    # while num >= 4:
    #     num -= 4
    #     res += 'IV'
    # while num > 0:
    #     num -= 1
    #     res += 'I'
    # return res


num = 1994
so = Solution()
print(so.intToRoman(num))
