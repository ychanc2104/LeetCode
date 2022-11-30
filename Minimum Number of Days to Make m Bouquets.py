# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/


# binary search, TC:O(NlogM) M is max of bloomDay, SC:O(1)
def minDays(bloomDay: List[int], m: int, k: int) -> int:
    def countBloom(day): # TC:O(N)
        count = 0
        consecutive = 0
        for d in bloomDay:
            if d <= day:
                consecutive += 1
            else:
                consecutive = 0
            if consecutive == k:
                count += 1
                consecutive = 0
        return count

    if len(bloomDay) < m * k: return -1
    L, R = 1, max(bloomDay)
    while L <= R:
        mid = (L + R) // 2
        if countBloom(mid) >= m:
            R = mid - 1
        else:
            L = mid + 1
    return L