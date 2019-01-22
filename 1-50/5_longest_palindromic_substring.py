class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            tmp = find_palin(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            tmp = find_palin(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

def find_palin(s, l, k):
        while l >= 0 and k < len(s) and s[l] == s[k]:
            l -= 1
            k += 1
        return s[l+1 : k]

input = "babad"
solution = Solution()
print(solution.longestPalindrome(input))