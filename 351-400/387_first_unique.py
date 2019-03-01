class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = [i]
            else:
                d[s[i]].append(i)
        rlt = []
        for key, value in d.items():
            if len(value) == 1:
                rlt.append(value[0])
        if not rlt:
            return -1
        return min(rlt)

print(Solution().firstUniqChar(""))