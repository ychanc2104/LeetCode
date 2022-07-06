# https://leetcode.com/problems/clone-graph/
# https://leetcode.com/problems/clone-graph/discuss/42314/Python-solutions-(BFS-DFS-iteratively-DFS-recursively).
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import collections

# first thought
def cloneGraph(node):
    if not node:
        return None
    stack = [node]
    visit = set()
    copy = dict()
    while stack:
        temp = stack.pop()
        if temp.val not in visit:
            visit.add(temp.val)
            stack.extend(temp.neighbors)
        if temp not in copy:
            copy[temp] = Node(temp.val)
            copy[temp].neighbors = []
        neighbors = []
        for n in temp.neighbors:
            # print(f'tmep: {temp.val}','neighbors', n.val)
            if n not in copy:
                copy[n] = Node(n.val)
                copy[n].neighbors = []
            neighbors.append(copy[n])
        copy[temp].neighbors = neighbors
    # test = copy[node].neighbors[0]
    # print(test,node.neighbors[0], test.val, test.neighbors[0].val, test.neighbors[1].val)
    return copy[node]

# improve, BFS, use .pop() is DFS(LIFO)
def cloneGraph2(node):
    if not node:
        return None
    queue = collections.deque([node])  # faster for pop() and append() than list
    visit = set()
    copy = dict()
    while queue:
        temp = queue.popleft() # FIFO
        # create copy if not existing
        if temp not in copy:
            copy[temp] = Node(temp.val)
        # if this node is not visited, create deep copy of node to the copy
        if temp.val not in visit:
            visit.add(temp.val)
            queue.extend(temp.neighbors)
            for n in temp.neighbors:
                # print(f'tmep: {temp.val}','neighbors', n.val)
                if n not in copy:
                    copy[n] = Node(n.val)
                copy[temp].neighbors.append(copy[n])
    # test = copy[node].neighbors[0]
    # print(test,node.neighbors[0], test.val, test.neighbors[0].val, test.neighbors[1].val)
    return copy[node]


# DFS, recursive
def cloneGraph3(node):
    nodes = {}
    if not node:
        return None
    def dfs(node):
        if node in nodes:
            return nodes[node]
        copy = Node(node.val)
        nodes[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy

    return dfs(node)

# DFS, iterative, TC:O(V+E), SC:O(N) for visit, O(h) for stack, h is height of graph
def cloneGraph4(node):
    if not node: return None
    memo = {}
    visit = set()
    stack = [node]
    while stack:
        temp = stack.pop()
        # assign copy of temp (not include neighbors)
        if temp not in memo:
            memo[temp] = Node(temp.val, neighbors=[])
        # control loop to terminate
        if temp.val not in visit:
            visit.add(temp.val)
            stack.extend(temp.neighbors)
            # assign its neighbors
            for n in temp.neighbors:
                if n not in memo:
                    # can be visited next round
                    memo[n] = Node(n.val, neighbors=[])
                memo[temp].neighbors.append(memo[n])
    return memo[node]