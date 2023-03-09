# https://leetcode.com/problems/minimum-time-to-complete-trips/description/


# sort and binary search, TC:O(NlogM) M = min time * totalTrips, SC:O(N)
def minimumTime(time: List[int], totalTrips: int) -> int:

    def finishable(x):
        trip = 0
        for t in time:
            trip += x // t
            if trip >= totalTrips:
                return True
        return False

    L, R = 0, min(time) * totalTrips
    while L <= R:
        mid = (L + R) // 2
        if finishable(mid):  # try smaller
            R = mid - 1
        else:
            L = mid + 1
    return L