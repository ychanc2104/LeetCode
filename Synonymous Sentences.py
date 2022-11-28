# https://leetcode.com/problems/synonymous-sentences/?envType=study-plan&id=graph-ii
# https://leetcode.com/problems/synonymous-sentences/solutions/430489/python-union-find/

import collections

# union find + dfs + sort, TC:O(), SC:O()
def generateSentences(synonyms: List[List[str]], text: str) -> List[str]:
    text_list = text.split(' ')

    # union all, and group parent:[word1, word2,...]
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        px, py = find(x), find(y)
        parents[px] = py

    parents = [i for i in range(2 * len(synonyms))]
    memo, idx = {}, 0  # word:idx
    for a, b in synonyms:
        if a not in memo:
            memo[a] = idx
            idx += 1
        if b not in memo:
            memo[b] = idx
            idx += 1
        union(memo[a], memo[b])
    table = collections.defaultdict(list)  # store all similar words
    for word, i in memo.items(): # TC:O(N*alpha(N))
        table[find(i)].append(word)

    def dfs(pos, sentence):
        if pos == len(text_list):
            res.append(' '.join(sentence))
            return
        if text_list[pos] not in memo:  # no need to change
            dfs(pos + 1, sentence + [text_list[pos]])
        else:  # change by all similar words
            for simi in table[find(memo[text_list[pos]])]:
                dfs(pos + 1, sentence + [simi])

    res = []
    dfs(0, [])
    return sorted(res)  # sort in the end

# union find + backtracking + sort, TC:O(), SC:O()
def generateSentences2(synonyms: List[List[str]], text: str) -> List[str]:
    text_list = text.split(' ')
    # union all, and group parent:[word1, word2,...]
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]
    def union(x, y):
        px, py = find(x), find(y)
        parents[px] = py
    parents = [i for i in range(2*len(synonyms))]
    memo, idx = {}, 0 # word:idx
    for a,b in synonyms:
        if a not in memo:
            memo[a] = idx
            idx += 1
        if b not in memo:
            memo[b] = idx
            idx += 1
        union(memo[a], memo[b])
    table = collections.defaultdict(list) # store all similar words
    for word,i in memo.items(): # TC:O(N*alpha(N))
        table[find(i)].append(word)

    def backtrack(pos=0):
        if pos == len(text_list):
            res.append(' '.join(path))
            return
        if text_list[pos] not in memo: # no need to change
            path.append(text_list[pos])
            backtrack(pos+1)
            path.pop()
        else: # change by all similar words
            for simi in table[find(memo[text_list[pos]])]:
                path.append(simi)
                backtrack(pos+1)
                path.pop()
    res = []
    path = []
    backtrack()
    return sorted(res) # sort in the end