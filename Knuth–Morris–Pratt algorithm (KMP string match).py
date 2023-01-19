# https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

# match s1 and s1 in TC:O(M+N) not TC:O(MN)

# create look-up table
# cacacabc

# s = "cacacabc" # 0,0,1,2,3,4,0,1
s = "aabaaabaaac" # 0,1,0,1,2,2,3,4,5,6,0
table = [0] * len(s) # 0,0,1,2,3,4,0,1

for i in range(1, len(s)):
    idx = table[i-1] # check s[idx] == s[i]
    while idx > 0 and s[i] != s[idx]: # if not match,
        idx = table[idx-1] # go to previous matched pos
    table[i] = idx + (s[i]==s[idx]) # add one



def strStr(haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle)
    failure_fun = [0] * m

    # abaaba => [0,0,1,1,2,1]
    for i in range(1, m):
        idx = failure_fun[i-1]
        while idx > 0 and needle[i] != needle[idx]:
            idx = failure_fun[idx-1] # try next match or not
        failure_fun[i] = idx + (needle[i]==needle[idx])
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
                j += 1 # move to next str in haystack
            else:
                k = failure_fun[k - 1] # move to previous
    return -1 # not matched