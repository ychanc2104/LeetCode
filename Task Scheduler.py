# https://leetcode.com/problems/task-scheduler/
# https://leetcode.com/problems/task-scheduler/discuss/760569/C%2B%2B-Greedy-O(n)-time-O(1)-space-with-explanation-in-5-lines.

import collections
import heapq


# TC:O(N), SC:O(26) ~ O(1)
def leastInterval(tasks, n: int) -> int:
    counter = collections.defaultdict(int)
    for t in tasks:
        counter[t] += 1
    n_freq = max(counter.values())
    n_occu = sum([x == n_freq for x in counter.values()])

    return max(len(tasks), (n_freq - 1) * (n + 1) + n_occu)


# heap, TC:O(Nlog26) = O(N), SC:O(26) = O(1)
def leastInterval2(tasks: List[str], n: int) -> int:
    counter = collections.Counter(tasks)

    heap = [-v for v in counter.values()]
    heapq.heapify(heap)
    res = 0
    while heap:
        temp = []
        idle = n + 1
        while idle > 0 and heap:
            v = -heapq.heappop(heap)
            v -= 1
            idle -= 1
            if v > 0:
                temp.append(-v)

        res += n + 1 - idle if not temp else n + 1
        [heapq.heappush(heap, t) for t in temp]
    return res