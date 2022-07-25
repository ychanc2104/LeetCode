# https://leetcode.com/problems/group-anagrams/

import collections

# TC:O(NKlogK), K is average length of str in strs, SC:O(K) or O(NK) for memo
def groupAnagrams(strs):
    memo = {}
    for word in strs:
        # TC:O(klogk) or replace with counting sort
        key = ''.join(sorted(word))
        if key not in memo.keys():
            memo[key] = [word]
        else:
            memo[key].append(word)
    return memo.values()

# TC:O(NK), K is average length of str in strs, TC:O(NK)
def groupAnagrams2(strs):
    memo = collections.defaultdict(list)
    for word in strs:
        counter = [0] * 26
        for c in word:
            counter[ord(c) - ord("a")] += 1
        memo[tuple(counter)].append(word)
    return memo.values()

strs = ["eat","tea","tan","ate","nat","bat"]

anagrams = list(groupAnagrams(strs))