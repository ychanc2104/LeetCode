# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/solutions/978984/python-rabin-karp/

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

# use Rabin-Karp rolling hash, TC:O(), SC:O(1)
def strStr(haystack: str, needle: str) -> int:
    def f(c):
        return ord(c)-ord('A')

    n, h, d, m = len(needle), len(haystack), 26, float("inf")
    if n > h: return -1
    nd, hash_n, hash_h = d**(n-1), 0, 0
    for i in range(n):
        hash_n = (d*hash_n+f(needle[i]))%m
        hash_h = (d*hash_h+f(haystack[i]))%m
    if hash_n == hash_h: return 0
    for i in range(1, h-n+1):
        hash_h = (d*(hash_h-f(haystack[i-1])*nd)+f(haystack[i+n-1]))%m    # e.g. 10*(1234-1*10**3)+5=2345
        if hash_n == hash_h: return i
    return -1