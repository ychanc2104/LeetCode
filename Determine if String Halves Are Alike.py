# https://leetcode.com/problems/determine-if-string-halves-are-alike/description/

# TC:O(N), SC:O(1)
def halvesAreAlike(s: str) -> bool:
    mid = len(s) // 2 - 1
    count = 0
    vowels_set = set('aeiouAEIOU')
    for i in range(len(s)):
        if s[i] not in vowels_set: continue
        count += 1 if i <= mid else -1
    return count == 0