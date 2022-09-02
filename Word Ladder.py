# https://leetcode.com/problems/word-ladder/


import collections


# bfs, first thought, TC:O(N*M^2), SC:O(N*M^2)
def ladderLength(beginWord: str, endWord: str, wordList) -> int:
    # bfs of each word,

    # build adjacency list
    graph = collections.defaultdict(list)
    # TC:O(N*M*M)
    for word in wordList:
        for i in range(len(word)):
            # copy str tack TC O(M)
            pattern = word[:i] + '*' + word[i + 1:]
            graph[pattern].append(word)
    # print(graph)
    # do bfs from beginWord, level-order
    queue = [beginWord]
    res = 1
    visit = set([beginWord])
    # traverse all nodes, O(N), everytime need to check pattern, O(M*M), so total TC:O(N*M^2)
    while queue:
        res += 1
        leafs = []
        for word in queue:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                for neighbor in graph[pattern]:
                    if neighbor == endWord:
                        return res
                    if neighbor in visit:
                        continue
                    leafs.append(neighbor)
                    visit.add(neighbor)
        queue = leafs
    return 0