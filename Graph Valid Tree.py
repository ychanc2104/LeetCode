# https://leetcode.com/problems/graph-valid-tree/
# https://leetcode.com/problems/graph-valid-tree/discuss/69046/Python-solution-with-detailed-explanation


import collections

# graph + dfs, TC:O(n+E), SC:O(n+E)
def validTree(n: int, edges) -> bool:
    if len(edges) != n - 1:
        return False
    # build graph
    graph = collections.defaultdict(list)
    # TC:O(E)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    stack = [0]
    parent = {0: -1}  # no parent
    # TC:O(n), traverse all nodes
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            # all nodes connecting to node
            if neighbor == parent[node]:
                continue
            if neighbor in parent:
                # cycle detection
                return False
            parent[neighbor] = node
            stack.append(neighbor)

    # print(graph, parent)
    return len(parent) == n


# advanced graph + dfs, TC:O(n+E), SC:O(n+E)
def validTree2(n: int, edges) -> bool:    # cycle check
    if len(edges)!=n-1:
        return False
    # build graph
    graph = collections.defaultdict(list)
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
    #print(graph)
    stack = [0]
    seen = {0}
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            # all nodes connecting to node
            if neighbor in seen:
                continue
            seen.add(neighbor)
            stack.append(neighbor)
    #print(graph, parent)
    return len(seen)==n



# union find, TC:O(n*alpha(n)) alpha(n) is inverse Ackermann function, SC:O(n)
def validTree3(n: int, edges) -> bool:  # cycle check
    if len(edges) != n - 1:
        return False
    parents = list(range(n))
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]
    def union(x, y):
        parents[find(x)] = find(y)

    for a, b in edges:
        union(a, b)
    for i in range(n):
        find(i)
    return len(set(parents)) == 1

# dfs, TC:O(n+E), SC:O(n+E)
def validTree4(n: int, edges) -> bool:    # cycle check
    # no loops and repeated edges
    # no repeat edges
    if len(edges) != n - 1:
        return False
    # no loops, visit all node from arbtary node
    # build graph(adjacency list)
    graph = collections.defaultdict(set)
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)

    # dfs
    visit = set()

    def dfs(node):
        if node in visit:
            return False
        visit.add(node)
        for nei in graph[node]:
            # remove node in nei, prevent go back
            graph[nei].remove(node)
            if not dfs(nei):
                return False
        return True

    if not dfs(0):
        return False
    return n == len(visit)




n = 5
edges = [[0,1],[1,2],[2,3],[1,3]]

