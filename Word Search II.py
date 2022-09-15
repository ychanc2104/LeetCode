# https://leetcode.com/problems/word-search-ii/
import time, collections
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


class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.isWord = False

    def insert(self, word):
        root = self
        for s in word:
            root = root.children[s]
        root.isWord = True
        root.word = word

# TC:O(M(4*3^(L-1))), M is number of cells and L is max length of words(first time with 4 direction and latter only has 3 dir), SC:O(n)
def findWords3(board, words):
    n = len(board)
    m = len(board[0])

    def dfs(i, j, node):
        if node.isWord:
            res.append(node.word)
            # prevent double adding
            node.isWord = False

        # boundary check
        if i < 0 or i >= n or j < 0 or j >= m:
            return
        char = board[i][j]
        if char not in node.children:
            return
        # mark visited
        board[i][j] = '#'
        # explore four directions
        new_node = node.children[char]
        dfs(i + 1, j, new_node)
        dfs(i - 1, j, new_node)
        dfs(i, j + 1, new_node)
        dfs(i, j - 1, new_node)
        # recover
        board[i][j] = char

        # (optimization) prune the nodes if reach end
        if not new_node.children:
            del node.children[char]
    # build trie
    trie = Trie()
    for word in words:
        trie.insert(word)
    res = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(i, j, trie)
    return res

# TC:O(M(4*3^(L-1))), M is number of cells and L is max length of words(first time with 4 direction and latter only has 3 dir), SC:O(n)
def findWords4(board, words):
    WORD_KEY = '$'
    trie = {}
    for word in words:
        node = trie
        for letter in word:
            # retrieve the next node; If not found, create a empty node.
            node = node.setdefault(letter, {})
        # mark the existence of a word in trie node
        node[WORD_KEY] = word
    rowNum = len(board)
    colNum = len(board[0])
    matchedWords = []

    def backtracking(row, col, parent):
        letter = board[row][col]
        currNode = parent[letter]
        # check if we find a match of word
        word_match = currNode.pop(WORD_KEY, False)
        if word_match:
            # also we removed the matched word to avoid duplicates,
            #   as well as avoiding using set() for results.
            matchedWords.append(word_match)
        # Before the EXPLORATION, mark the cell as visited
        board[row][col] = '#'
        # Explore the neighbors in 4 directions, i.e. up, right, down, left
        for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            newRow, newCol = row + rowOffset, col + colOffset
            if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                continue
            if not board[newRow][newCol] in currNode:
                continue
            backtracking(newRow, newCol, currNode)
        # End of EXPLORATION, we restore the cell
        board[row][col] = letter
        # Optimization: incrementally remove the matched leaf node in Trie.
        if not currNode:
            parent.pop(letter)

    for row in range(rowNum):
        for col in range(colNum):
            # starting from each of the cells
            if board[row][col] in trie:
                backtracking(row, col, trie)

    return matchedWords




board = [["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"]]
words = ["ababababaa","ababababab","ababababac","ababababad","ababababae","ababababaf","ababababag","ababababah","ababababai","ababababaj","ababababak","ababababal","ababababam","ababababan","ababababao","ababababap","ababababaq"]


board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain","oathi","oathk","oathf","oate","oathii","oathfi","oathfii"]

WORD_KEY = '$'

trie = {}
for word in words:
    node = trie
    for letter in word:
        # retrieve the next node; If not found, create a empty node.
        node = node.setdefault(letter, {})
    # mark the existence of a word in trie node
    node[WORD_KEY] = word


res3 = findWords3(board, words)
#
trie = Trie()
for word in words:
    trie.insert(word)
#
res = findWords(board, words)

res2 = Solution().findWords2(board, words)

