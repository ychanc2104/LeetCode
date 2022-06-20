# https://leetcode.com/problems/implement-trie-prefix-tree/
# https://leetcode.com/problems/implement-trie-prefix-tree/discuss/1509720/C%2B%2BPython-208.-Implement-Trie-(Prefix-Tree)-Clean-and-Concise
from collections import defaultdict

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie) # generate Trie class if key not exist
        self.isWord = False

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


#
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie2:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for s in word:
            if s not in node.children:
                node.children[s] = TrieNode()
            node = node.children[s]
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for w in prefix:
            if w not in node.children:
                return False
            node = node.children[w]
        return True


trie = Trie()
trie.insert('apple')
trie.insert('app')
trie.search('app')

b = Trie2()


b.insert('apple')
b.insert('app')
b.insert('add')
b.insert('ad')
b.insert('applepie')
b.insert('dead')




b.search('apple')
b.startsWith('app')