class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        else:
            positive = (dividend >= 0) is (divisor > 0)
            dividend, divisor, res = abs(dividend), abs(divisor), 0
            for i in range(32)[::-1]:
                if dividend - (divisor << i) >= 0:
                    res += (1 << i)
                    dividend -= (divisor << i)
        return res if positive else -res
