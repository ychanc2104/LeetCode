# https://leetcode.com/problems/possible-bipartition/

import collections

# union find, TC:O(N+M), SC:O(N+M)
def possibleBipartition(n: int, dislikes: List[List[int]]) -> bool:
    graph = {i: [] for i in range(n + 1)}  # SC:O(M)
    for a, b in dislikes:
        graph[a].append(b)
        graph[b].append(a)

    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    # only two groups, so all neighbors should be in one group
    parents = [i for i in range(n + 1)]  # SC:O(N)
    for node, neis in graph.items():  # TC:O(V+E) = O(N+M), SC:O(N+M)
        pnode = find(node)
        # union all neis together because node and neis should be partitioned into two groups
        for i in range(1, len(neis)):
            pnei = find(neis[i])
            parents[find(neis[0])] = pnei  # union
            if pnode == pnei:  # confilct with original node
                return False
    return True

# union find with rank compression, TC:O(N+M), SC:O(N+M)
def possibleBipartition2(n: int, dislikes: List[List[int]]) -> bool:
    graph = {i:[] for i in range(n+1)} # SC:O(M)
    for a,b in dislikes:
        graph[a].append(b)
        graph[b].append(a)
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]
    # only two groups, so all neighbors should be in one group
    parents = [i for i in range(n+1)] # SC:O(N)
    ranks = [0] * (n+1)
    for node,neis in graph.items(): # TC:O(V+E) = O(N+M), SC:O(N+M)
        pnode = find(node)
        # union all neis together because node and neis should be partitioned into two groups
        for i in range(1,len(neis)):
            pnei = find(neis[i])
            p0 = find(neis[0])
            if ranks[p0] > ranks[pnei]:
                parents[pnei] = p0 # union
            elif ranks[p0] < ranks[pnei]:
                parents[p0] = pnei # union
            else:
                parents[p0] = pnei # union
                ranks[pnei] += 1
            if pnode == pnei: # confilct with original node
                return False
    return True


# BFS, TC:O(N+M), SC:O(N+M)
def possibleBipartition3(n: int, dislikes: List[List[int]]) -> bool:
    graph = {i: [] for i in range(n + 1)}  # SC:O(M)
    for a, b in dislikes:
        graph[a].append(b)
        graph[b].append(a)
    colors = [0] * (n + 1)  # 0,1,-1 0,1 are the two groups
    for i in range(1, n + 1):
        # do bfs or dfs and start coloring
        if colors[i]: continue
        colors[i] = 1
        queue = collections.deque([i])
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                if colors[node] == colors[nei]:  # should not be in same group => conflict
                    return False
                if not colors[nei]:  # not coloring yet
                    colors[nei] = -colors[node]
                    queue.append(nei)
    return True



# DFS, TC:O(N+M), SC:O(N+M)
def possibleBipartition4(n: int, dislikes: List[List[int]]) -> bool:
    graph = {i:[] for i in range(n+1)} # SC:O(M)
    for a,b in dislikes:
        graph[a].append(b)
        graph[b].append(a)
    def dfs(node):
        for nei in graph[node]:
            if colors[node] == colors[nei]:
                return False
            if colors[nei] == -1:
                colors[nei] = 1 - colors[node]
                if not dfs(nei):
                    return False
        return True
    colors = [-1] * (n+1) # 0,1,-1 0,1 are the two groups
    for i in range(1, n+1):
        # do bfs or dfs and start coloring
        if colors[i] != -1: continue
        colors[i] = 1
        if not dfs(i):
            return False
    return True