import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for s in word:
            current = current.children[s]  #这样可以初始化
        current.is_word = True

    def search(self, word):
        current = self.root
        for s in word:
            current = current.children.get(s) #这样得到的是None
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix):
        current = self.root
        for s in prefix:
            current = current.children.get(s)
            if current is None:
                return False
        return True