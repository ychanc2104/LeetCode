# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

# binary search, TC:O(NlogN), SC:O(1)
def shipWithinDays(weights: List[int], days: int) -> int:
    def check(x) -> bool:
        tempSum = 0
        day = 1
        for w in weights:
            if w > x: return False
            if tempSum + w > x:
                day += 1
                tempSum = w
            else:
                tempSum += w
        return day <= days

    L, R = 0, sum(weights)
    while L <= R:
        mid = L + (R - L) // 2
        if check(mid):  # decrease x
            R = mid - 1
        else:
            L = mid + 1
    return L
