# https://leetcode.com/problems/the-maze-iii/
# https://leetcode.com/problems/the-maze-iii/solutions/150550/python-short-priorityqueue-solution-beats-100/

import heapq

# Dijkstra + 2d dp, TC:O(NMlogNM), SC:O(NM)
def findShortestWay(maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
    n, m = len(maze), len(maze[0])
    heaps = [(0, [], ball)]  # step, instructions, position
    dp = {tuple(ball): [0, []]}  # step,pattern
    while heaps:
        step, instructions, (r, c) = heapq.heappop(heaps)
        if [r, c] == hole: return ''.join(instructions)
        for ro, co, ins in ((1, 0, 'd'), (0, 1, 'r'), (-1, 0, 'u'), (0, -1, 'l')):
            rn, cn, temp_step = r, c, step
            while 0 <= rn + ro < n and 0 <= cn + co < m and maze[rn + ro][cn + co] == 0:
                rn += ro
                cn += co
                temp_step += 1
                if [rn, cn] == hole: break  # reach hole
            if (rn, cn) not in dp or dp[(rn, cn)] > [temp_step,
                                                     instructions]:  # smaller step or (equal step and smaller instructions) found
                pattern = instructions + [ins]
                dp[(rn, cn)] = [temp_step, pattern]
                heapq.heappush(heaps, (temp_step, pattern, (rn, cn)))
    return 'impossible'


def findShortestWay2(A: List[List[int]], ball: List[int], hole: List[int]) -> str:
    ball, hole = tuple(ball), tuple(hole)
    R, C = len(A), len(A[0])

    def neighbors(r, c):
        for dr, dc, di in [(-1, 0, 'u'), (0, 1, 'r'),
                           (0, -1, 'l'), (1, 0, 'd')]:
            cr, cc, dist = r, c, 0
            while (0 <= cr + dr < R and
                   0 <= cc + dc < C and
                   not A[cr + dr][cc + dc]):
                cr += dr
                cc += dc
                dist += 1
                if (cr, cc) == hole:
                    break
            yield (cr, cc), di, dist

    pq = [(0, '', ball)]
    seen = set()
    while pq:
        dist, path, node = heapq.heappop(pq)
        if node in seen: continue
        if node == hole: return path
        seen.add(node)
        for nei, di, nei_dist in neighbors(*node):
            heapq.heappush(pq, (dist + nei_dist, path + di, nei))

    return "impossible"


# Dijkstra, no need to use dp, TC:O(NMlogNM), SC:O(NM)
def findShortestWay3(maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
    n, m = len(maze), len(maze[0])
    heaps = [(0, [], ball)]  # step, instructions, position
    seen = set() # record hitting wall
    # position
    while heaps:
        step, instructions, (r, c) = heapq.heappop(heaps)
        if (r, c) in seen: continue
        seen.add((r, c))
        if [r, c] == hole: return ''.join(instructions)
        for ro, co, ins in ((1, 0, 'd'), (0, 1, 'r'), (-1, 0, 'u'), (0, -1, 'l')):
            rn, cn, temp_step = r, c, step
            while 0 <= rn + ro < n and 0 <= cn + co < m and maze[rn + ro][cn + co] == 0:
                rn += ro
                cn += co
                temp_step += 1
                if [rn, cn] == hole: break  # reach hole
            pattern = instructions + [ins]
            heapq.heappush(heaps, (temp_step, pattern, (rn, cn)))
    return 'impossible'