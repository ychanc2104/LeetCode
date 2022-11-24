# https://leetcode.com/problems/koko-eating-bananas/?envType=study-plan&id=binary-search-ii

# binary search, TC:O(NlogM), SC:O(1)
def minEatingSpeed(piles: List[int], h: int) -> int:
    def check(k):
        hour = 0
        for pile in piles:
            hour += (pile - 1) // k + 1
        return hour

    # (L,R,mid) (1,11,6)=>(1,5,3)=>(4,5,4)8=>(4,3) stop
    L, R = 1, max(piles)
    while L <= R:
        mid = (L + R) // 2
        if check(mid) > h:  # increase L
            L = mid + 1
        else:
            R = mid - 1
    return L