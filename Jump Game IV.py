# https://leetcode.com/problems/jump-game-iv/

import collections

# BFS, clear memo to prevent redundant search, TC:O(N), SC:O(N)
def minJumps(arr: List[int]) -> int:
    # BFS
    memo = collections.defaultdict(list)
    for i, num in enumerate(arr):
        memo[num].append(i)

    step = 0
    queue = collections.deque([(0, step)])
    visited = set([0])
    while queue:
        i, step = queue.popleft()
        if i == len(arr) - 1: return step
        for nei in memo[arr[i]]:
            if nei in visited: continue

            visited.add(nei)
            queue.append((nei, step + 1))
        memo[arr[i]] = []  # this value is done
        for nei in [i - 1, i + 1]:
            if nei < 0 or nei >= len(arr) or nei in visited: continue
            visited.add(nei)
            queue.append((nei, step + 1))

# BFS, another set to prevent redundant search, TC:O(N), SC:O(N)
def minJumps2(arr: List[int]) -> int:
    memo = collections.defaultdict(list)
    for i, num in enumerate(arr):
        memo[num].append(i)

    step = 0
    queue = collections.deque([(0, step)])
    visited = set([0])
    visited_value = set()
    while queue:
        i, step = queue.popleft()
        if i == len(arr) - 1: return step
        for nei in [i - 1, i + 1]:
            if nei < 0 or nei >= len(arr) or nei in visited: continue
            visited.add(nei)
            queue.append((nei, step + 1))
        if arr[i] in visited_value: continue
        visited_value.add(arr[i])
        # skip below if same value encounter
        for nei in memo[arr[i]]:
            if nei in visited: continue
            visited.add(nei)
            queue.append((nei, step + 1))

# BFS, TC:O(N), SC:O(N)
def minJumps3(arr: List[int]) -> int:

    jump = collections.defaultdict(list)
    n = len(arr)
    for i in range(n):
        jump[arr[i]].append(i)
    queue = collections.deque([(0, 0)])  # idx, step
    visited = [True] + [False] * (n - 1)

    while queue:

        idx, step = queue.popleft()
        if idx == n - 1:
            return step
        for nei in [idx - 1, idx + 1]:
            if not 0 <= nei < n or visited[nei]: continue
            visited[nei] = True
            queue.append((nei, step + 1))

        while jump[arr[idx]]:
            nei = jump[arr[idx]].pop()
            if visited[nei]: continue
            visited[nei] = True
            queue.append((nei, step + 1))