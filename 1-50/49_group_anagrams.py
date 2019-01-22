class Solution(object):
    def groupAnagrams(self, strs):
        res = {}
        for w in strs:
            key = tuple(sorted(w))
            res[key] = res.get(key, []) + [w]
        return res.values()

put = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(put))