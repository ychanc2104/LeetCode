# https://leetcode.com/problems/group-anagrams/

def groupAnagrams(strs):
    memo = {}
    for word in strs:
        word_list = list(word)
        word_list.sort()
        key = ''.join(word_list)
        if key not in memo.keys():
            memo[key] = [word]
        else:
            memo[key].append(word)
    return memo.values()


strs = ["eat","tea","tan","ate","nat","bat"]

anagrams = list(groupAnagrams(strs))