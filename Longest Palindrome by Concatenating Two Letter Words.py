# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description/

import collections

# hash table to store freq, TC:O(N+min(N, 26^2)), SC:O(min(N, 26^2))
def longestPalindrome(words: List[str]) -> int:
    res = 0
    counter = collections.Counter(words)  # O(N), SC:O(min(N, 26^2))
    is_central = False
    for word, c in counter.items(): # min(N, 26^2) size
        if word[0] == word[1]:  # repeated words
            if c & 1:  # odd
                res += c - 1  # dd
                is_central = True
            else:
                res += c
        elif word[0] > word[1]:  # do not double counting
            res += 2 * min(counter[word], counter[word[::-1]])
    if is_central:
        res += 1
    return res * 2

