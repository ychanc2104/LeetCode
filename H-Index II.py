# https://leetcode.com/problems/h-index-ii/

# binary search, TC:O(logN), SC:O(1)
def hIndex(citations: List[int]) -> int:
    # there are h papers at least cited h times
    L, R = 0, len(citations) - 1
    while L <= R:
        mid = (L + R) // 2  # citations[mid] is trial h index
        if len(citations) - mid == citations[mid]:
            return citations[mid]
        if len(citations) - mid < citations[mid]:  # h is too big, decrease R
            R = mid - 1
        else:
            L = mid + 1
    return len(citations) - L  # len(citations) - L papers with at least cited h


# binary search, TC:O(logN), SC:O(1)
def hIndex2(citations: List[int]) -> int:
    # h in range of [0,len(citations)]
    # there are h papers at least cited h times
    L ,R = 0, len(citations)-1
    while L <= R:
        mid = (L + R)//2 # citations[mid] is trial h index
        if len(citations) - mid <= citations[mid]: # h is too big, decrease R
            R = mid - 1
        else:
            L = mid + 1
    return len(citations) - L # len(citations) - L papers with at least cited h