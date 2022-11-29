# https://leetcode.com/problems/maximum-number-of-removable-characters/description/

# first thought, binary search, TC:O(NlogM) N is length of s and M is length of removable, SC:O(M)
def maximumRemovals(s: str, p: str, removable: List[int]) -> int:
    # check
    def check(k): # TC:O(N), SC:O(k)
        remove = set(removable[:k])
        pos = 0
        for i in range(len(s)):
            if i in remove: continue
            if s[i] == p[pos]:
                pos += 1
            if pos == len(p): return True
        return False

    # TTFF
    L, R = 0, len(removable)
    while L <= R: # TC:O(logM)
        mid = (L + R) // 2
        if check(mid):  # is subsequence, increase L
            L = mid + 1
        else:
            R = mid - 1
    return R