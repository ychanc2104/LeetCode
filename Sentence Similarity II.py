# https://leetcode.com/problems/sentence-similarity-ii/?envType=study-plan&id=graph-ii


# first thought, union find, TC:O(M*alpha(N) + N), SC:(N)
def areSentencesSimilarTwo(sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
    if len(sentence1) != len(sentence2): return False
    words = [word for pair in similarPairs for word in pair]
    words = list(set(words))
    parents = [i for i in range(len(words))]
    memo = {word: i for i, word in enumerate(words)}

    # print(memo)
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        px, py = find(x), find(y)
        parents[px] = py

    for a, b in similarPairs:
        union(memo[a], memo[b])

    for w1, w2 in zip(sentence1, sentence2):
        if w1 == w2: continue
        if w1 not in memo or w2 not in memo or find(memo[w1]) != find(memo[w2]):
            return False
    return True


# concise union find, TC:O(M*alpha(N) + N), SC:(N)
def areSentencesSimilarTwo2(sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
    if len(sentence1) != len(sentence2): return False
    parents = [i for i in range(2 * len(similarPairs))]  # upper bound

    # print(memo)
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        px, py = find(x), find(y)
        parents[px] = py
    # do union find and build memo at a time
    memo = {}
    idx = 0
    for a, b in similarPairs:
        if a not in memo:
            memo[a] = idx
            idx += 1
        if b not in memo:
            memo[b] = idx
            idx += 1
        union(memo[a], memo[b])

    for w1, w2 in zip(sentence1, sentence2):
        if w1 == w2: continue
        if w1 not in memo or w2 not in memo or find(memo[w1]) != find(memo[w2]):
            return False
    return True