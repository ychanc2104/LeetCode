# https://leetcode.com/problems/concatenated-words/
# https://leetcode.com/problems/concatenated-words/solutions/159348/python-dfs-readable-solution/

# dfs + dp, TC:O(NM^3) N is length of words and M is length of word, SC:O(M*N) for words set
def findAllConcatenatedWordsInADict(words: List[str]) -> List[str]:
    words_set = set(words)

    def dfs(word):
        for i in range(1, len(word)): # TC:O(M*M^2) str_slice(M) * edges(M^2), M is length of word
            prefix = word[:i]
            suffix = word[i:]
            if prefix in words_set and suffix in words_set:
                return True
            elif prefix in words_set and dfs(suffix):
                return True
        return False

    res = []
    for i, word in enumerate(words):
        if dfs(word):
            res.append(word)
    return res