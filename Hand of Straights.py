# https://leetcode.com/problems/hand-of-straights/?envType=daily-question&envId=2024-06-06

import collections

# TC:O(MlogM + N) ~ O(NlogN), SC:O(N)
def isNStraightHand(hand: List[int], groupSize: int) -> bool:
    n = len(hand)
    if n % groupSize != 0:
        return False
    counter = collections.Counter(hand)
    for k in sorted(counter):
        while counter.get( k -1, 0) == 0 and counter[k] != 0:
            l = 0
            num = k
            while num in counter and counter[num] != 0 and l < groupSize:
                counter[num] -= 1
                l += 1
                num += 1
            if l != groupSize:
                return False
    return all(v==0 for v in counter.values())

# TC:O(N) ~ O(NlogN), SC:O(N)
def isNStraightHand2(hand: List[int], groupSize: int) -> bool:
    n = len(hand)
    if n % groupSize != 0:
        return False
    counter = collections.Counter(hand)
    for num in counter:
        # find start of a group
        start = num
        while counter[start-1]:
            start -= 1
        # find groups until start count == 0 and all group after start
        while start <= num:
            while counter[start] != 0:
                for i in range(start, start+groupSize):
                    if counter[i] == 0:
                        return False
                    counter[i] -= 1
            start += 1
    return True