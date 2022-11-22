# https://leetcode.com/problems/redundant-connection-ii/
# https://leetcode.com/problems/redundant-connection-ii/solutions/108058/one-pass-disjoint-set-solution-with-explain/
# https://leetcode.com/problems/redundant-connection-ii/solutions/108045/c-java-union-find-with-explanation-o-n/

# union find, TC:O(N), SC:O(N)
def findRedundantDirectedConnection1(edges: list[list[int]]) -> list[int]:
    cand1, cand2, memo = None, None, {}
    for a, b in edges: # a point to b
        if b in memo:  # don't point to the same node
            cand1, cand2 = [memo[b], b], [a, b] # first and second(last edges if cycle)
            break
        memo[b] = a

    # union find
    parents = [i for i in range(len(edges))]

    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]

    for x, y in edges:
        if [x, y] == cand2:
            continue
        px, py = find(x - 1), find(y - 1)
        if px == py:
            return cand1 if cand1 else [x, y]
        parents[py] = px # union
    return cand2


edges = [[1,4],[3,4],[1,3],[1,2],[4,5]]

res = findRedundantDirectedConnection1(edges)
