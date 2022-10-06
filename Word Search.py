# https://leetcode.com/problems/word-search/


import collections


# faster, remove some cases word count>board
def exist1(board, word: str) -> bool:
    m = len(board)
    n = len(board[0])
    k = len(word)
    visit = set()

    def dfs(index, target):
        r, c = index
        # print(index, target, visit)
        if target == k:
            return True
        if r > m - 1 or c > n - 1 or r < 0 or c < 0 or target > k - 1 or index in visit or board[r][c] != word[target]:
            return False

        visit.add((r, c))
        # print(index, target, visit)
        res = dfs((r, c + 1), target + 1) or dfs((r + 1, c), target + 1) or dfs((r - 1, c), target + 1) or dfs(
            (r, c - 1), target + 1)
        visit.remove((r, c))
        return res

    ## remove word letter count > in board
    word_count = collections.Counter(word)
    board_count = collections.Counter(''.join([w for row in board for w in row]))
    # print(word_count, board_count)
    for key, value in word_count.items():
        # print(key, value, board_count[key])
        if value > board_count[key]:
            return False

    for i in range(m):
        for j in range(n):
            if dfs((i, j), 0):
                return True
    return False


# fastest
def exist2(board, word: str) -> bool:
    m = len(board)
    n = len(board[0])
    k = len(word)
    visit = set()

    def dfs(index, target):
        r, c = index
        # print(index, target, visit)
        if target == k:
            return True
        if r > m - 1 or c > n - 1 or r < 0 or c < 0 or target > k - 1 or index in visit or board[r][c] != word[target]:
            return False

        visit.add((r, c))
        # print(index, target, visit)
        res = dfs((r, c + 1), target + 1) or dfs((r + 1, c), target + 1) or dfs((r - 1, c), target + 1) or dfs(
            (r, c - 1), target + 1)
        visit.remove((r, c))
        return res

    ## remove word letter count > in board
    word_count = collections.Counter(word)
    board_count = collections.Counter(''.join([w for row in board for w in row]))
    # print(word_count, board_count)
    for key, value in word_count.items():
        # print(key, value, board_count[key])
        if value > board_count[key]:
            return False

    ###### key section here ######
    ## reverse if last word is more frequently appear
    if word_count[word[0]] > word_count[word[-1]]:
        word = word[::-1]

    for i in range(m):
        for j in range(n):
            if dfs((i, j), 0):
                return True
    return False



# the fastest, remove some cases word count>board
def exist3(board, word: str) -> bool:
    ROW = len(board)
    CELL = len(board[0])
    path = set()
    def dfs(x, y, i):
        if i == len(word):
            return True
        if (x, y) in path: return False
        # if board[x][y] == "#": return False
        # within matrix
        if x < 0 or y < 0 or x >= ROW or y >= CELL:
            return False
        # if current board letter does not match current word letter
        if board[x][y] != word[i]:
            return False
        path.add((x, y))
        # temp = board[x][y]
        # board[x][y] = "#"
        res = dfs(x + 1, y, i + 1) or dfs(x - 1, y, i + 1) or dfs(x, y - 1, i + 1) or dfs(x, y + 1, i + 1)
        # board[x][y] = temp
        path.remove((x, y))
        return res
    # Create hash table and store  letter = freq of appearance
    hm_board = {}
    for i in range(ROW):
        for j in range(CELL):
            # get returns value of board[i][j] if exist, otherwise second parm ie 0 will be used.
            hm_board[board[i][j]] = hm_board.get(board[i][j], 0) + 1
    # print(hm_board)
    # construct hashtable from word letter letter = freq of appearance
    hm_word = collections.Counter(word)
    # compare board letter freqs to word letter freqs
    # if board does not have enough letter to makeup the word.. exit.
    for char, freq in hm_word.items():
        # print(char, "=>" , hm_board.get(char, 0), freq)
        if hm_board.get(char, 0) < freq:
            return False

    # check the freqs of the first letter of the world to last
    # if less, reverse word
    # print(hm_word[word[0]], hm_word[word[-1]], word[::-1])
    if hm_word[word[0]] > hm_word[word[-1]]:
        word = word[::-1]
    for x in range(ROW):
        for y in range(CELL):
            if dfs(x, y, 0):
                return True
    return False




# dfs + backtracking, TC:O(N*M*3^L), SC:O(L), L = len(word) for recursive call
def exist4(board, word: str) -> bool:
    n, m = len(board), len(board[0])

    def dfs(pos, i, j):
        if pos >= len(word):
            return True
        if i < 0 or j < 0 or i >= n or j >= m or board[i][j] != word[pos]:
            return False

        letter = board[i][j]
        board[i][j] = '#'  # mark visited
        for ro, co in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            res = dfs(pos + 1, i + ro, j + co)
            if res:  # once true, no need to explore more
                break
        board[i][j] = letter  # backtrack
        return res

    # remove case, freq of board < freq of word
    counter_1 = collections.Counter([s for row in board for s in row])
    counter_2 = collections.Counter(word)
    if not all([counter_1[k] >= counter_2[k] for k in counter_2]):
        return False
    # TC:O(NM3^K)
    for i in range(n):
        for j in range(m):
            if dfs(0, i, j):
                return True
    return False