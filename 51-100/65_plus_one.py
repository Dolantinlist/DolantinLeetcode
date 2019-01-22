class Solution(object):
    def plusOne(self, digits):
        l = len(digits)
        flag = True
        for i in digits:
            if i != 9:
                flag = False
                break
        if flag:
            return [1] + [0] * l

        for i in range(l - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0

        return digits


print(Solution().plusOne([9,9,9]))