import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = collections.Counter(t)
        rlt = ''
        l = len(s) + 1
        left, right = 0, 0
        while right < len(s) + 1:
            flag = True
            for key in dic:
                if dic[key] > 0:
                    flag = False
                    break
            if flag:
                if right - left < l:
                    l = right - left
                    rlt = s[left: right]
                if s[left] in dic:
                    dic[s[left]] += 1
                left += 1
            else:
                if right == len(s):
                    break
                if s[right] in dic:
                    dic[s[right]] -= 1
                right += 1
        return rlt

print(Solution().minWindow("DEBANC", "ABC"))