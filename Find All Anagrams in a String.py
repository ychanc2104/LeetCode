# https://leetcode.com/problems/find-all-anagrams-in-a-string/


import collections

# first thought, permutations, time exceed
def findAnagrams(s: str, p: str):
    if len(p) > len(s):
        return []

    def get_permutations(p):
        res = []

        def dfs(pos):
            if pos == len(p):
                res.append(''.join(p))

            for i in range(pos, len(p)):
                p[i], p[pos] = p[pos], p[i]
                dfs(pos + 1)
                p[i], p[pos] = p[pos], p[i]

        dfs(0)
        return res

    permute = set(get_permutations(list(p)))
    # print(permute)
    res = []
    for i in range(len(s)):
        if s[i:i + len(p)] in permute:
            res.append(i)
    return res

# sliding window, TC:O(n), SC:O(26) ~ O(1)
def findAnagrams2(s: str, p: str):
    if len(p) > len(s):
        return []
    # initialize s[:len(p]
    counter = collections.Counter(p)
    for i in range(len(p)):
        counter[s[i]] -= 1
    res = []
    if all([v == 0 for v in counter.values()]):
        res.append(0)
    # O(n)
    for i in range(len(p), len(s)):
        # print(counter, s[i])
        counter[s[i]] -= 1
        counter[s[i - len(p)]] += 1
        # TC: O(26)
        if all([v == 0 for v in counter.values()]):
            res.append(i - len(p) + 1)
    return res

s = "cbaebabacd"
p = "ab"



