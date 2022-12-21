# https://leetcode.com/problems/time-needed-to-inform-all-employees/
# https://leetcode.com/problems/time-needed-to-inform-all-employees/solutions/532560/java-c-python-dfs/


import collections

# first thought, DFS, TC:O(N), SC:O(N)
def numOfMinutes(n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    # need to spread, return longest path(last person to receive information)
    # do DFS
    graph = collections.defaultdict(list)
    for i, man in enumerate(manager): # TC:O(N), SC:O(N)
        graph[man].append(i)
    pathSum = [0]
    res = [0]

    def dfs(node): # TC:O(V+E) = O(N+N-1)
        if not graph[node]:  # reach end
            res[0] = max(res[0], pathSum[0])
            return
        for nei in graph[node]:
            pathSum[0] += informTime[node]
            dfs(nei)
            pathSum[0] -= informTime[node]

    dfs(headID)
    return res[0]


# DFS, TC:O(N), SC:O(N)
def numOfMinutes2(n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    # need to spread, return longest path(last person to receive information)
    # do DFS
    def dfs(node): # time of node receiving information
        if manager[node] == -1:
            return informTime[node] # directly return
        informTime[node] += dfs(manager[node])
        manager[node] = -1 # mark visited
        return informTime[node]
    return max(map(dfs, range(n)))