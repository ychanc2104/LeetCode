# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/
# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/solutions/197668/count-the-number-of-islands-o-n/


# first thought, union find, TC:O(N^2*alpha(N)), SC:O(N)
def removeStones(stones: List[List[int]]) -> int:
    # union find
    parents = [i for i in range(len(stones))]

    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        px, py = find(x), find(y)
        parents[px] = parents[py]

    for i in range(len(stones)):
        for j in range(i + 1, len(stones)):
            x1, y1 = stones[i]
            x2, y2 = stones[j]
            if x1 == x2 or y1 == y2:
                union(i, j)
    [find(i) for i in range(len(stones))]
    return len(stones) - len(set(parents))

# optimized union find, TC:O(N*alpha(N)), SC:O(N)
def removeStones2(stones: List[List[int]]) -> int:
    # union find
    parents = {}

    def find(x):
        px = parents.setdefault(x, x)
        if x != px:
            parents[x] = find(px)
        return parents[x]

    def union(x, y):
        px, py = find(x), find(y)
        parents[px] = py

    for x, y in stones:
        # union x and y, ~y = -(y+1) a kind of ego (transformation)
        union(x, ~y)  # transform to differentiate row and col
    return len(stones) - len({find(i) for i in parents})  # total stones - number of connected components