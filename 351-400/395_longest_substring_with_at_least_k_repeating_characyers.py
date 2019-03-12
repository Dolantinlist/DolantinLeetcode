import collections
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        lookup = collections.Counter(s)
        for c in lookup:
            if lookup[c] < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)