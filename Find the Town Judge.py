# https://leetcode.com/problems/find-the-town-judge/description/
#

# directed graph, TC:O(N), SC:O(N)
def findJudge(n: int, trust: List[List[int]]) -> int:
    indegrees = {i: 0 for i in range(1, n + 1)} # prevent trust = []
    for a, b in trust:
        indegrees[b] += 1  # be trusted
        indegrees[a] -= 1  # trust others

    for i, c in indegrees.items():
        if c == n - 1:
            return i
    return -1