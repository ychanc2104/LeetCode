# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/?envType=study-plan&id=graph-ii


# union find, TC:O(N+MlogM+Malpha(N)), SC:O(N+M)
def earliestAcq(logs: List[List[int]], n: int) -> int:
    # become a circlic graph
    parents = [i for i in range(n)] # TC:O(N), SC:O(N)

    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    count = n
    logs.sort(key=lambda x: x[0]) # should be sorted by timestamp, TC:O(MlogM), SC:O(M)
    for ts, a, b in logs: # TC:O(M)
        pa, pb = find(a), find(b) # TC:O(alpha(N))
        if pa == pb:  # duplicate friend
            continue
        parents[pa] = pb
        count -= 1
        if count == 1:  # one group remaining
            return ts
    return -1