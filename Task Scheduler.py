# https://leetcode.com/problems/task-scheduler/
# https://leetcode.com/problems/task-scheduler/discuss/760569/C%2B%2B-Greedy-O(n)-time-O(1)-space-with-explanation-in-5-lines.

import collections

# TC:O(N), SC:O(26) ~ O(1)
def leastInterval(tasks, n: int) -> int:
    counter = collections.defaultdict(int)
    for t in tasks:
        counter[t] += 1
    n_freq = max(counter.values())
    n_occu = sum([x == n_freq for x in counter.values()])

    return max(len(tasks), (n_freq - 1) * (n + 1) + n_occu)

