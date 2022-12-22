# https://leetcode.com/problems/sum-of-distances-in-tree/
# https://leetcode.com/problems/sum-of-distances-in-tree/solutions/130583/c-java-python-pre-order-and-post-order-dfs-o-n/

import collections

# postorder dfs + preorder dfs, TC:O(N), SC:O(N)
def sumOfDistancesInTree(n: int, edges: List[List[int]]) -> List[int]:
    # res[i] = res[root] + count(i) + (N - count(i)), root is root node of i node
    # build count[i]: how many nodes of i's children
    graph = collections.defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    res = [0] * n
    count = [1] * n  # count[i]: how many nodes of i's children

    def dfs(pre=-1, root=0):  # postorder
        for nei in graph[root]:
            if nei == pre: continue  # don't go back, look for its children
            dfs(root, nei)
            count[root] += count[nei]
            res[root] += res[nei] + count[nei] # build correct res[0], distance of root = dist of nei + number of nei's nodes

    def dfs2(pre=-1, root=0):  # preorder
        for nei in graph[root]:
            if nei == pre: continue  # don't go back, look for its children
            res[nei] = res[root] - count[nei] + (n - count[nei]) # first update 0's children
            dfs2(root, nei)

    dfs() # build correct res[0]
    print(count, res)
    dfs2()
    return res