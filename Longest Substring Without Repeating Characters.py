# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/347818/Python3%3A-sliding-window-O(N)-with-explanation
import collections

# first thought, sliding window, TC:O(n), SC:O(n)
def lengthOfLongestSubstring(s: str) -> int:
    # dvdf, (0,1), (1,2), (1,3)
    if len(s) <= 1: return len(s)
    L, R = 0, 1
    counter = collections.Counter(s[L])
    res = 0
    while R < len(s):
        counter[s[R]] += 1
        # make window valid
        while counter[s[R]] > 1:
            counter[s[L]] -= 1
            L += 1
        res = max(res, R - L + 1)
        R += 1
    return res

