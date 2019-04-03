class Solution:
    def __init__(self):
        self.a = []
        self.d = {}

    def Insert(self, char):
        self.a.append(char)
        if char in self.d:
            self.d[char] += 1
        else:
            self.d[char] = 1

    def FirstAppearingOnce(self):
        for ch in self.a:
            if self.d[ch] == 1:
                return ch
        return '#'