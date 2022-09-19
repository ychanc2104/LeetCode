# https://leetcode.com/problems/alien-dictionary/

import collections

# TC:O(C+V+E) ~ O(C), O(V+E), O(E) is O(U+min(26^2,N-1)), N is len(words) and N-1 is number of adjacent pairs
# C is total number of string, U is number of unique letter
# SC:O(V+E)=> O(U + min(U^2, N-1)), U can be 26, a constant
def alienOrder(words) -> str:
    # build adjacency list
    adj = collections.defaultdict(set)
    # TC:O(N), N is total number of characters
    in_degree = {c: 0 for word in words for c in word}  # initial value
    # TC:O(N) in total
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        # check from first char
        for j in range(min(len(w1), len(w2))):
            c1, c2 = w1[j], w2[j]
            if c1 != c2:
                # don't count same pair
                if c2 not in adj[c1]:
                    in_degree[c2] += 1
                adj[c1].add(c2)
                break
        else:
            # not break => all characters are the same
            if len(w1) > len(w2):
                # not valid, w2 is prefix of w1
                return ''
    # print(adj, in_degree)
    # start from in_degree == 0
    queue = collections.deque([k for k, v in in_degree.items() if v == 0])
    # print(queue)
    res = []
    while queue:
        char = queue.popleft()
        res.append(char)
        for neighbor in adj[char]:
            # char -> neighbor
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    if not all([v == 0 for v in in_degree.values()]):
        # cyclic detection
        return ""
    return ''.join(res)




for a,b in zip((1,2,3),(3,2)):
    print(a,b)