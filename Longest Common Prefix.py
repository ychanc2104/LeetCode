# https://leetcode.com/problems/longest-common-prefix/




# first though, error occur many times,
# TC: O(mn) ~ O(S), S is all characters in strs, ST: O(1)
def longestCommonPrefix(strs) -> str:
    s = strs.pop()
    res = ''
    i = 0
    # O(m), m is length of strs[i]
    while i < len(s) and strs:
        sub = s[i]
        # O(n), n is len(strs)
        if all([len(x) > i and x[i] == sub for x in strs]):
            i += 1
            res = s[:i]
        else:
            return res
    return res if strs else s


# use zip, TC: O(S), ST: O(m), m is length of strs[i]
def longestCommonPrefix2(strs) -> str:
    res = ''
    for x in zip(*strs):
        if len(set(x)) == 1:
            # all the same
            res += x[0]
        else:
            return res
    return res

# use zip, TC:O(S), ST:O(1)
def longestCommonPrefix3(strs) -> str:
    i = 0
    for x in zip(*strs):
        if len(set(x)) == 1:
            # all the same
            i += 1
        else:
            return strs[0][:i]
    return strs[0][:i]


def longestCommonPrefix4(strs) -> str:
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest