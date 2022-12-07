# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/
# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/solutions/402401/python-use-topologically-sorted-items-and-groups-to-get-the-desired-order/

import collections


# topsort, TC:O(NM), SC:O(N+M)
def sortItems(n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
    # sort group first and sort inner group items, pre-assign -1 to new group
    # 1. assign -1 to new group
    for i in range(n): # TC:O(N)
        if group[i] == -1:
            group[i] = m
            m += 1
    # 2. build two graph
    graph_b = collections.defaultdict(list)
    graph_g = collections.defaultdict(list)
    indegrees_b = {i: 0 for i in range(n)} # SC:O(N)
    indegrees_g = {i: 0 for i in range(m)} # SC:O(M)
    for i in range(n): # TC:O(NM)
        for b in beforeItems[i]:
            graph_b[b].append(i)
            indegrees_b[i] += 1
            if group[i] == group[b]: continue
            # add to graph_g
            graph_g[group[b]].append(group[i])
            indegrees_g[group[i]] += 1

    # print(graph_b, graph_g, indegrees_b, indegrees_g)
    # topsort helper function
    def topsort(graph, indegrees):
        res = []
        queue = collections.deque([node for node, count in indegrees.items() if count == 0])
        count = len(indegrees.keys())
        while queue:
            node = queue.popleft()
            res.append(node)
            count -= 1
            for nei in graph[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)
        return res if count == 0 else []

    # 3. do topsort
    topo_b = topsort(graph_b, indegrees_b) # TC:O(N)
    topo_g = topsort(graph_g, indegrees_g) # TC:O(M)
    # print(topo_b, topo_g)
    # 4. sort inner groups items
    memo = collections.defaultdict(list) # SC:O(N)
    for i in topo_b:
        memo[group[i]].append(i)
    # print(memo)
    # 5. sort by groups
    res = []
    for g in topo_g:
        res.extend(memo[g])
    return res