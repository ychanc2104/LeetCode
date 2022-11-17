# https://leetcode.com/problems/analyze-user-website-visit-pattern/description/
# https://leetcode.com/problems/analyze-user-website-visit-pattern/solutions/709445/python3-accepted/

import collections

# use combinations
def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
    def comb(array, k):
        res = []
        path = []
        def backtrack(pos=0):
            if len(path) == k:
                res.append(tuple(path[:]))
                return
            for i in range(pos, len(array)):
                path.append(array[i])
                backtrack(i + 1)
                path.pop()

        backtrack()
        return res

    users = collections.defaultdict(list)
    for u, t, w in sorted(zip(username, timestamp, website)):
        users[u].append(w)
    pattern = {}
    for websites in users.values():
        for c in set(comb(websites, 3)):
            pattern[c] = pattern.get(c, 0) + 1
    res = []
    count = 0
    for k, v in pattern.items():
        if v > count:
            res = k
            count = v
        elif v == count and k < res: # lexicographically smallest pattern
            res = k
    return res
