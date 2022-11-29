# https://leetcode.com/problems/similar-string-groups/


# first thought, union find, TC:O((alpha(N)+M)N^2), SC:O(N)
def numSimilarGroups(strs: List[str]) -> int:
    # check each pair
    def check(s1, s2):
        res = []
        for i, (l1, l2) in enumerate(zip(s1, s2)):
            if l1 == l2: continue
            res.append(i)
        if len(res) == 2:
            L, R = res
            return s1[L] == s2[R] and s1[R] == s2[L]
        return False if res else True

    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        px, py = find(x), find(y)
        parents[px] = py

    parents = [i for i in range(len(strs))]
    for i in range(len(strs) - 1):
        for j in range(i + 1, len(strs)):
            s1, s2 = strs[i], strs[j]
            if check(s1, s2):
                union(i, j)

    return len(set([find(i) for i in range(len(strs))]))

# optimized union find, TC:O((alpha(N)+M)N^2), SC:O(N)
def numSimilarGroups2(strs: List[str]) -> int:
    # check each pair
    def check(s1, s2):
        count = 0
        for i, (l1, l2) in enumerate(zip(s1, s2)):
            if l1 == l2: continue
            count += 1
            if count > 2: return False
        return True

    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        px, py = find(x), find(y)
        if rank[px] == rank[py]:
            parents[px] = py
            rank[py] += 1
        elif rank[px] > rank[py]:  # small to big
            parents[py] = px
        else:
            parents[px] = py

    parents = [i for i in range(len(strs))]
    rank = [0] * len(strs)
    for i in range(len(strs) - 1): # TC:O((alpha(N)+M)N^2)
        for j in range(i + 1, len(strs)):
            s1, s2 = strs[i], strs[j]
            if check(s1, s2): # TC:O(M)
                union(i, j) # TC:O(alpha(N))
    return len(set([find(i) for i in range(len(strs))])) # TC:O(N*alpha(N))