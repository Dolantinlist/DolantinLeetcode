class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        l = len(endWord)
        if beginWord in wordList:
            wordList.remove(beginWord)
        result = 2
        step, next, end, wordSet = set([beginWord]), set([]), set([endWord]), set(wordList)
        while len(step):
            for word in step:
                for i in range(l):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        tmp = str(word[:i]) + ch + str(word[i+1:])
                        if tmp in wordSet:
                            next.add(tmp)
            if len(next & end):
                return result
            step, next = next, set([])
            result += 1
            if len(step) > len(end):
                step, end = end, step
            wordSet -= step
        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(Solution().ladderLength(beginWord, endWord, wordList))