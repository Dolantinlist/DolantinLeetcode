from collections import Counter
from copy import deepcopy
def findSubstring(s, words):
    res = []
    m, n, k = len(s), len(words), len(words[0])
    cnt = Counter(words)
    for i in range(k):
        tmp = deepcopy(cnt)
        start = i
        for j in range(start, m - k + 1, k):
            word = s[j:j+k]
            tmp[word] -= 1
            while tmp[word] < 0:
                tmp[s[start:start+k]] += 1
                start += k
            if j + k -start == n*k:
                res.append(start)
    return res

s = "barfoothefoobarman"
words = ["foo","bar"]
print(findSubstring(s, words))