# https://leetcode.com/problems/find-players-with-zero-or-one-losses/

import collections

# first thought, hash + sort, TC:O(nlogn), SC:O(n)
def findWinners(matches: List[List[int]]) -> List[List[int]]:
    counter = collections.defaultdict(int)  # player: count of loss
    for w, l in matches:
        counter[w] += 0
        counter[l] += 1
    res = [[], []]
    for player, count in counter.items():
        if count == 0:
            res[0].append(player)
        elif count == 1:
            res[1].append(player)
    res[0].sort()
    res[1].sort()
    return res