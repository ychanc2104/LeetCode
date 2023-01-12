# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/solutions/624141/clean-python-3-peel-onion-in-o-n-100-time-space/
# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/solutions/3033301/python3-dfs-explained/?orderBy=most_votes


import collections

# first thought, topsort, TC:O(N+M), SC:O(N+M)
def minTime(n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
    # topsort, if hasApple[node] => res += 2
    graph = collections.defaultdict(list)
    indegrees = {i: 0 for i in range(n)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
        indegrees[a] += 1
        indegrees[b] += 1
    queue = collections.deque([node for node, v in indegrees.items() if v == 1])
    res = 0
    while queue:
        node = queue.popleft()
        if node == 0: continue
        for nei in graph[node]:
            indegrees[nei] -= 1  # drop node
            if hasApple[node]:
                res += 2
                hasApple[nei] = True
                hasApple[node] = False
            if indegrees[nei] == 1:
                queue.append(nei)
    return res

def minTime2(n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
    # topsort, if hasApple[node] => res += 2
    graph = collections.defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node=0, parent=-1):  # return time from node to get all of children's apples
        totalTime, childTime = 0, 0
        for nei in graph[node]:
            if nei == parent: continue  # reach end, if no apple in path, return 0
            childTime = dfs(nei, node)
            if hasApple[nei] or childTime:
                totalTime += childTime + 2
        return totalTime

    return dfs()