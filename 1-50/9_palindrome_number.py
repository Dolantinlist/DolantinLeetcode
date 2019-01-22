class Solution:
    def isPalindrome(self, x):
        s = list(str(x))
        l = len(s)
        if s[0] == '-':
            return False
        else:
            flag = True
            for i in range(int(l/2) + 1):
                if s[i] != s[l-i-1]:
                    flag = False
                    break

        return flag


input = -1234321
print(Solution().isPalindrome(input))