class Solution:
    def minMutation(self, start, end, bank):
        bank = set(bank)
        change = {"A" : "CGT", "C" : "AGT", "G" : "ACT", "T" : "ACG"}
        tmp = [[start, 0]]
        for node in tmp:
            if node[0] == end :
                return node[1]
            for i, c in enumerate(node[0]):
                for s in change[c]:
                    nxt = node[0][:i] + s + node[0][i+1:]
                    if nxt in bank:
                        tmp.append([nxt, node[1]+1])
                        bank.remove(nxt) #重要
        return -1