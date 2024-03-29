# https://leetcode.com/problems/implement-trie-prefix-tree/
# https://leetcode.com/problems/implement-trie-prefix-tree/discuss/1509720/C%2B%2BPython-208.-Implement-Trie-(Prefix-Tree)-Clean-and-Concise
from collections import defaultdict

# use dict only
class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        root = self.root
        for c in word:
            if c not in root:
                root[c] = {}
            root = root[c]
        root['#'] = True

    def search(self, word: str) -> bool:
        root = self.root
        for c in word:
            if c not in root:
                return False
            root = root[c]
        return '#' in root

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for c in prefix:
            if c not in root:
                return False
            root = root[c]
        return True

class Trie2:
    def __init__(self):
        self.children = defaultdict(Trie) # generate Trie class if key not exist
        self.isWord = False
    # TC:O(m), m is len(word), SC:O(m)
    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.isWord = True
    # TC:O(m), m is len(word), SC:O(1)
    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord

    # TC:O(m), m is len(word), SC:O(1)
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

class Trie3:
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