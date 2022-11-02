# https://leetcode.com/problems/minimum-genetic-mutation/description/

import collections

# first thought, bfs, TC:O(N), SC:O(N), N is bank length, string length is 8
def minMutation(start: str, end: str, bank: List[str]) -> int:
    # from start to end and the path must in the bank, return numbers
    # graph, bfs? explore all paths
    def count_diff(s, t):
        count = 0
        for si, ti in zip(s, t):
            if si != ti:
                count += 1
        return count

    queue = collections.deque([(start, 0)])
    visit = set()
    while queue:
        node, step = queue.popleft()
        if node in visit: continue
        visit.add(node)
        if node == end: return step
        for b in bank:
            if count_diff(node, b) == 1:
                queue.append((b, step + 1))
    return -1


# early return, bfs, TC:O(N), SC:O(N), N is bank length, string length is 8
def minMutation2(start: str, end: str, bank: List[str]) -> int:
    # from start to end and the path must in the bank, return numbers
    # graph, bfs? explore all paths
    queue = collections.deque([(start, 0)])
    visit = set()
    while queue:
        node, step = queue.popleft()
        if node in visit: continue
        visit.add(node)
        if node == end: return step
        for b in bank:
            count = 0
            for si, ti in zip(node, b):
                if si != ti:
                    count += 1
                if count > 1: break
            if count == 1:
                queue.append((b, step+1))
    return -1