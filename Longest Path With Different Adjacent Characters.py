# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/description/
# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/solutions/1955433/java-c-python-dfs-on-tree/
# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/solutions/3042992/python3-dfs-explained/

import collections


# dfs, TC:O(NlogN) with sort, SC:O(N)

def longestPath(parent: List[int], s: str) -> int:
    res = [1]
    graph = collections.defaultdict(list)
    for node, p in enumerate(parent):
        if p == -1: continue
        graph[node].append(p)
        graph[p].append(node)

    def dfs(node=0, parent=-1):  # return max path
        candidates = []
        for child in graph[node]:
            if child == parent: continue  # don't go back to parent
            temp = dfs(child, node)
            if s[node] != s[child]:  # no adjacent node is the same char
                candidates.append(temp)
        candidates.sort()
        res[0] = max(res[0], sum(candidates[-2:]) + 1)
        return (candidates[-1] if candidates else 0) + 1

    dfs()
    return res[0]

# dfs, TC:O(N) w/o sort, SC:O(N)
def longestPath2(parent: List[int], s: str) -> int:
    res = 1
    graph = collections.defaultdict(list)
    for node, p in enumerate(parent):
        if p == -1: continue
        graph[node].append(p)
        graph[p].append(node)

    def dfs(node=0, parent=-1):  # return max path
        nonlocal res
        max1 = max2 = 0
        for child in graph[node]:
            if child == parent: continue  # don't go back to parent
            temp = dfs(child, node)
            if s[node] != s[child]:  # no adjacent node is the same char
                if temp >= max1:
                    max1, max2 = temp, max1
                elif temp > max2:
                    max2 = temp
        res = max(res, max1 + max2 + 1)
        return max1 + 1

    dfs()
    return res

# dfs, TC:O(N) w/o sort, SC:O(N)
def longestPath3(parent: List[int], s: str) -> int:
    graph = collections.defaultdict(list)
    for i, p in enumerate(parent):
        if p == -1: continue
        graph[p].append(i)
    # print(graph)
    res = 1

    def dfs(node):
        nonlocal res

        first = second = 0
        for nei in graph[node]:
            if s[nei] == s[node]:
                dfs(nei)
            else:
                x = dfs(nei)
                if x > first:
                    first, second = x, first
                elif x > second:
                    second = x

        res = max(res, first + second + 1)
        return (first + 1)

    dfs(0)
    return res