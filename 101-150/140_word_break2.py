class Solution:
    def wordBreak(self, s: str, wordDict: [str]) ->[str]:
        memo = {}
        return self.helper(s, wordDict,memo)

    def helper(self, s: str, wordDict: [str], memo: dict) -> [str]:
        if s in memo:
            return memo[s]
        res =[]
        if not s:
            return res
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(s) == len(word):
                res.append(word)
            else:
                rest = self.helper(s[len(word):], wordDict, memo)
                for tmp in rest:
                    tmp = word + ' ' + tmp
                    res.append(tmp)
        memo[s] = res
        return res

s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(Solution().wordBreak(s, wordDict))
