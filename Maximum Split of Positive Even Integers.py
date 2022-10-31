# https://leetcode.com/problems/maximum-split-of-positive-even-integers/description/

# first thought, TC:O(sqrt(n)), SC:O(1)
def maximumEvenSplit(n: int):
    if n & 1: return []
    res = []
    i = 1
    while n != 0:
        if n - 2 * i >= 2 * (i + 1) or (n - 2 * i == 0):
            res.append(2 * i)
            n -= 2 * i
        i += 1
    return res


def maximumEvenSplit2(n: int):
    if n & 1: return []
    res = []
    for i in range(1,n//2+1):
        if n - 2*i >= 0:
            res.append(2*i)
            n -= 2*i
        else: # append remaining
            res[-1] += n
            return res
    return res