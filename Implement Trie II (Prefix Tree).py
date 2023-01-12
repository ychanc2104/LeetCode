# https://leetcode.com/problems/implement-trie-ii-prefix-tree/description/

# first thought, use dict
class Trie:

    def __init__(self):
        self.root = {} # node, isWord, count

    def insert(self, word: str) -> None:
        root = self.root
        for s in word:
            if s not in root:
                root[s] = {} # new node
            root = root[s]
        root['#'] = True # is word
        root['count'] = root.get('count', 0) + 1
        # print(self.root)
    def countWordsEqualTo(self, word: str) -> int:
        root = self.root
        for s in word:
            if s not in root:
                return 0
            root = root[s]
        return root.get('count', 0)
    def countWordsStartingWith(self, prefix: str) -> int:
        # count all child end nodes
        root = self.root
        for s in prefix:
            if s not in root:
                return 0
            root = root[s]
        res = 0
        def dfs(root):
            nonlocal res
            if root.get('#', False):
                res += root.get('count', 0)
            for node in root.keys():
                if node == '#' or node == 'count': continue
                dfs(root[node])
        dfs(root)
        return res
    def erase(self, word: str) -> None:
        root = self.root
        for s in word:
            if s not in root:
                break
            root = root[s]
        if root.get('count', 0) <= 1:
            root.pop('#', None)
            root.pop('count', None)
        else:
            root['count'] -= 1

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)