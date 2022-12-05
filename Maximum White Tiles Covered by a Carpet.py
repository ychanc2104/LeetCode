# https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/description/

# two pointer sliding window, TC:O(NlogN), SC:O(N) for sorting
def maximumWhiteTiles(tiles: List[List[int]], carpetLen: int) -> int:
    tiles.sort()
    # extend to max => move each tile one by one
    ps, pe = 0, 0
    cover = 0
    res = 0
    while pe < len(tiles) and res < carpetLen:
        if tiles[ps][0] + carpetLen > tiles[pe][1]: # extend end
            cover += tiles[pe][1] - tiles[pe][0] + 1
            pe += 1
            res = max(res, cover)
        else:  # move start pointer
            remain = max(0, tiles[ps][0] + carpetLen - tiles[pe][0])
            res = max(res, cover + remain)
            cover -= tiles[ps][1] - tiles[ps][0] + 1  # move start
            ps += 1
    return res


# prefix sum + binary search, TC:O(NlogN), SC:O(N) for sorting
def maximumWhiteTiles2(tiles: List[List[int]], carpetLen: int) -> int:
    tiles.sort()
    endPos = [e for s,e in tiles]
    def bsearch(target):
        L, R = 0, len(endPos)-1
        while L <= R:
            mid = (L + R)//2
            if endPos[mid] >= target:
                R = mid - 1
            else:
                L = mid + 1
        return L # leftmost
    prefix = [0]
    for s,e in tiles:
        prefix.append(prefix[-1] + e - s + 1)
    # print(prefix)
    n = len(tiles)
    res = 0
    for i in range(n):
        s, e = tiles[i]
        # find its final fully covered end
        idx = bsearch(s + carpetLen - 1) # if not existing, return bigger one [0,n]
        remain = max(0, (s + carpetLen - tiles[idx][0])) if idx < n else 0
        cover = (prefix[idx] - prefix[i]) if idx < n else prefix[-1] - prefix[i]
        res = max(res, cover + remain)
    return res