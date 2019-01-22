class Solution(object):
    def multiply_string(self, num1, num2):
        l = len(num1) + len(num2)
        res = [0] * l
        index = l
        for i in range(len(num1) - 1, -1, -1):
            index -= 1
            pos = index
            for j in range(len(num2) - 1, -1, -1):
                tmp = int(num1[i]) * int(num2[j])
                res[pos] += tmp
                res[pos - 1] += res[pos] // 10
                res[pos] %= 10
                pos -= 1

        start = 0
        while start < l and res[start] == 0:
            start += 1
        result = ''.join(map(str, res[start:]))
        if result == "":
            result = "0"
        return result

a = "123"
b = "456"
print(Solution().multiply_string(a, b))