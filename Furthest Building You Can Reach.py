# https://leetcode.com/problems/furthest-building-you-can-reach/description/

import heapq

# use heaps, TC:O(NlogN), SC:O(N)
def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
    # use bricks first
    heaps = []  # diff, idx
    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        if diff <= 0: continue
        heapq.heappush(heaps, (diff, i))
        if len(heaps) > ladders:
            d, idx = heapq.heappop(heaps)
            if bricks - d < 0:
                return i
            bricks -= d
    return len(heights) - 1

# binary search, TC:O(N(logN)^2), SC:O(N)
def furthestBuilding2(heights: List[int], bricks: int, ladders: int) -> int:
    # bsearch i
    def check(idx): # TC:O(NlogN)
        res = []
        for i in range(idx):
            diff = heights[i+1] - heights[i]
            if diff <= 0: continue
            res.append(diff)
        res.sort()
        bricks_remain = bricks
        ladders_remain = ladders
        for d in res:
            if bricks_remain-d >= 0:
                bricks_remain -= d
            elif ladders_remain-1 >= 0:
                ladders_remain -= 1
            else:
                return False # no bricks and ladders
        return True

    L, R = 0, len(heights)-1
    while L <= R:
        mid = (L + R) //2
        if check(mid): # can reach
            L = mid + 1
        else:
            R = mid - 1
    return max(L-1, 0)


# binary search, sort once => store index and diff beforehand, TC:O(NlogN), SC:O(N)
def furthestBuilding3(heights: List[int], bricks: int, ladders: int) -> int:
    # bsearch i
    diffs = [(heights[i+1]-heights[i], i) for i in range(len(heights)-1)]
    diffs.sort() # TC:O(NlogN)
    def check(idx): # TC:O(N)
        bricks_remain = bricks
        ladders_remain = ladders
        for d, i in diffs:
            if i >= idx or d <= 0: continue
            if bricks_remain-d >= 0:
                bricks_remain -= d
            elif ladders_remain-1 >= 0:
                ladders_remain -= 1
            else:
                return False # no bricks and ladders
        return True

    # TC:O(NlogN)
    L, R = 0, len(heights)-1
    while L <= R:
        mid = (L + R) //2
        # print(L,R,mid)
        if check(mid): # can reach
            L = mid + 1
        else:
            R = mid - 1
    return max(L-1, 0)