# https://leetcode.com/problems/design-search-autocomplete-system/description/


# first thought, use trie
class AutocompleteSystem:

    # TC:O(N), SC:O(N)
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = {} # root,count,@:word
        self.type = []
        for count,word in zip(times,sentences):
            self.add_word(word, count)

    # TC:O(N), SC:O(N)
    def add_word(self, word, count=1):
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['count'] = node.get('count', 0) + count
        node['@'] = word

    # TC:O(N), SC:O(N)
    def input(self, c: str) -> List[str]: # get all word,count at given prefix
        if c == '#':
            # add into trie
            self.add_word(''.join(self.type))
            self.type = []
            return []
        self.type.append(c)

        node = self.trie
        for c in self.type:
            if c not in node:
                return []
            node = node[c]
        # get all word
        words = []
        def dfs(node):
            if '@' in node:
                words.append([-node['count'], node['@']])
            for c in node.keys():
                if c in ['@', 'count']:
                    continue
                dfs(node[c])
        dfs(node)
        # print(words)
        return [w for c,w in sorted(words)[:3]]