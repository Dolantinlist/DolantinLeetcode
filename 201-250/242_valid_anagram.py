import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdic = collections.Counter(s)
        tdic = collections.Counter(t)
        for key in sdic:
            if key in tdic and tdic[key] == sdic[key]:
                continue
            return False
        for key in tdic:
            if key in sdic and sdic[key] == tdic[key]:
                continue
            return False
        return True