class Solution(object):
    def addBinary(self, a, b):
        a, b = [ord(ch) - 48 for ch in a[::-1]], [ord(ch) - 48 for ch in b[::-1]]
        carry, result, len_a, len_b = 0, ['0'] * max(len(a), len(b)), len(a), len(b)
        for i in range(max(len_a, len_b)):
            s = carry
            if i < len_a: s += a[i]
            if i < len_b: s += b[i]
            carry, remainder = divmod(s, 2)
            result[i] = chr(remainder + 48)
        if carry: result.append('1')
        return ''.join(result[::-1])


a = '11'
b = '1'
print(Solution().addBinary(a,b))