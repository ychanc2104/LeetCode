# https://leetcode.com/problems/word-search-ii/
import time
from functools import wraps

def timing(func):
    @wraps(func)
    def time_count(*args, **kwargs):
        t_start = time.time()
        values = func(*args, **kwargs)
        t_end = time.time()
        print (f"{func.__name__} time consuming:  {(t_end - t_start):.3f} seconds")
        return values
    return time_count


# first though, combine word search
@timing
def findWords(board, words):
    def wordSearch(board, word):
        n = len(board)
        m = len(board[0])
        visit = set()

        def dfs(row, col, i, visit):
            # true case
            if i >= len(word):
                return True
            # false case
            if row < 0 or col < 0 or row >= n or col >= m or board[row][col] != word[i] or (row, col) in visit:
                return False
            visit.add((row, col))
            ans = dfs(row - 1, col, i + 1, visit) or dfs(row + 1, col, i + 1, visit) or \
                  dfs(row, col - 1, i + 1, visit) or dfs(row, col + 1, i + 1, visit)
            visit.remove((row, col))
            return ans

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0, visit):
                    return True
        return False

    res = []
    for word in words:
        if wordSearch(board, word):
            res.append(word)
    return res


class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def insert(self, word):
        node = self
        for w in word:
            if w not in node.children:
                node.children[w] = Trie()
            node = node.children[w]
        node.isWord = True

class Solution:
    @timing
    def findWords2(self, board, words):
        # add all words into Trie
        self.n_words = len(words)
        trie = Trie()
        visit = set()
        res = []
        for word in words:
            trie.insert(word)

        def dfs(row, col, path, node):
            # end
            if self.n_words == 0:
                return
            # check is a word in words
            if node.isWord:
                res.append(path)
                # prevent double counting
                node.isWord = False
                self.n_words -= 1
            # backtrack
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or (row, col) in visit:
                return
            char = board[row][col]
            if char not in node.children:
                return
            visit.add((row, col))
            ## explore four directions
            dfs(row - 1, col, path + char, node.children[char])
            dfs(row + 1, col, path + char, node.children[char])
            dfs(row, col - 1, path + char, node.children[char])
            dfs(row, col + 1, path + char, node.children[char])
            visit.remove((row, col))

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, '', trie)
        return res

board = [["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"]]
words = ["ababababaa","ababababab","ababababac","ababababad","ababababae","ababababaf","ababababag","ababababah","ababababai","ababababaj","ababababak","ababababal","ababababam","ababababan","ababababao","ababababap","ababababaq"]

res = findWords(board, words)

res2 = Solution().findWords2(board, words)

