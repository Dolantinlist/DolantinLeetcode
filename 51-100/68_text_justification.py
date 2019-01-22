class Solution(object):
    def fullJustify(self, words, maxWidth):
        cur, res, num = [], [], 0
        for w in words:
            if len(cur) + len(w) + num > maxWidth:
                for i in range(maxWidth - num):
                    cur[i%((len(cur) - 1) or 1)] += ' '
                res.append(''.join(cur))
                cur = []
                num = 0
            cur += [w]
            num += len(w)

        return res  + [' '.join(cur).ljust(maxWidth)]


words = ["This", "is", "an", "example", "of", "text", "justification."]
print(Solution().fullJustify(words, 16))