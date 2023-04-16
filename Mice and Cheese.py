# https://leetcode.com/problems/mice-and-cheese/description/
# https://leetcode.com/problems/mice-and-cheese/solutions/3368322/java-c-python-k-largest-a-i-b-i/

import heapq

# sort and greedy, TC:O(NlogN), SC:O(N)
def miceAndCheese(reward1: List[int], reward2: List[int], k: int) -> int:
    res = sum(reward2)
    reward = sorted([w - reward2[i] for i, w in enumerate(reward1)])
    for i in range(k):
        diff = reward[~i]
        res += diff
    return res


# use heap, TC:O(Nlogk), SC:O(N)
def miceAndCheese(reward1: List[int], reward2: List[int], k: int) -> int:
    res = sum(reward2)
    reward = [-w+reward2[i] for i,w in enumerate(reward1)]
    heapq.heapify(reward)
    for i in range(k):
        res += -heapq.heappop(reward)
    return res