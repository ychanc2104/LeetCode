# https://leetcode.com/problems/design-add-and-search-words-data-structure/
# https://leetcode.com/problems/design-add-and-search-words-data-structure/discuss/59725/Python-easy-to-follow-solution-using-Trie.
# https://leetcode.com/problems/design-add-and-search-words-data-structure/discuss/774530/Python-Trie-solution-with-dfs-explained

import collections

class WordDictionary:

    def __init__(self):
        self.children = collections.defaultdict(WordDictionary)
        self.isWord = False

    def addWord(self, word: str) -> None:
        node = self
        for w in word:
            node = node.children[w]
        node.isWord = True
    def search(self, word: str) -> bool:
        self.res = False
        node = self
        def dfs(node, word):
            if not word:
                if node.isWord:
                    self.res = True
                # end if word is empty
                return
            # is '.' iterate all possible
            if word[0] == '.':
                for prefix in node.children.keys():
                    dfs(node.children[prefix], word[1:])
            # in children, iterate deeper
            elif word[0] in node.children:
                dfs(node.children[word[0]], word[1:])
            # end
            else:
                return
        dfs(node, word)
        return self.res

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


# faster to use addition TrieNode class
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary2:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isWord = True

    def search(self, word: str) -> bool:
        self.res = False
        node = self.root

        def dfs(node, word):
            if not word:
                if node.isWord:
                    self.res = True
                # end if word is empty
                return
            # is '.' iterate all possible
            if word[0] == '.':
                for prefix in node.children.keys():
                    dfs(node.children[prefix], word[1:])
            # in children, iterate deeper
            elif word[0] in node.children:
                dfs(node.children[word[0]], word[1:])
            # end
            else:
                return

        dfs(node, word)
        return self.res

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


class TrieNode:
    def __init__(self):
        self.hashmap = {}
        self.end = False

class WordDictionary3:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.hashmap:
                current.hashmap[c] = TrieNode()
            current = current.hashmap[c]
        current.end = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            current = node
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for char in current.hashmap.values():
                        if dfs(i + 1, char):
                            return True
                    return False
                else:
                    if c not in current.hashmap:
                        return False
                    current = current.hashmap[c]
            return current.end

        return dfs(0, self.root)