# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/


# Knuth-Morris-Pratt algorithm(KMP), TC:O(M+N), SC:O(M)
def strStr(haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle)
    failure_fun = [0] * m

    # abaaba => [0,0,1,1,2,1]
    prev = 0
    i = 1
    while i < m:
        if needle[i] == needle[prev]:
            prev += 1
            failure_fun[i] = prev
            i += 1
        else:
            if prev == 0:
                i += 1
            else:
                prev = failure_fun[prev - 1]
    j = 0  # haystack pointer
    k = 0  # needle pointer
    while j < n:
        if haystack[j] == needle[k]:
            j += 1
            k += 1
            if k == m:  # finish
                return j - m
        else:
            if k == 0:
                j += 1
            else:
                k = failure_fun[k - 1]
    return -1