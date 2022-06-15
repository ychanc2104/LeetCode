# https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import defaultdict

# neetcode solution, TC: O(n)
def characterReplacement(s: str, k: int) -> int:
    L = 0
    res = 0
    # count for substring
    counter = {}
    # L, R is close form
    for R in range(len(s)):
        counter[s[R]] = 1 + counter.get(s[R], 0)
        # while loop to keep s[L:R+1] valid
        # while loop can be replaced with if else because no need to look for length of substring smaller than current R-L-1
        while (R - L + 1) - max(counter.values()) > k:
            counter[s[L]] -= 1
            L += 1
        res = max(res, R - L + 1)
    return res

# modified neetcode solution, TC: O(n)
def characterReplacement2(s: str, k: int) -> int:
    L = 0
    res = 0
    # count for substring
    counter = {}
    # L, R is close form
    for R in range(len(s)):
        counter[s[R]] = 1 + counter.get(s[R], 0)
        # while loop to keep s[L:R+1] valid
        max_count = max(max_count, counter[s[R]])
        while (R - L + 1) - max_count > k:
            counter[s[L]] -= 1
            L += 1
        res = max(res, R - L + 1)
    return res

# modified neetcode solution, TC: O(n), the fastest
def characterReplacement3(s: str, k: int) -> int:
    L = 0
    res = 0
    max_count = 0
    # count for substring
    counter = {}
    # L, R is close form
    for R in range(len(s)):
        counter[s[R]] = 1 + counter.get(s[R], 0)
        # while loop to keep s[L:R+1] valid
        max_count = max(max_count, counter[s[R]])
        if (R - L + 1) - max_count > k:
            counter[s[L]] -= 1
            L += 1
        else:
            res = max(res, R - L + 1)
    return res




def characterReplacement4(s: str, k: int) -> int:
    # Max_length the longest subsequence without repeating chars and k changes
    # Max_count is the high count chars in the answer subsequence
    max_length = max_count = 0
    # Count keeps track of the chars in the we are looking at subsequence
    count = defaultdict(int)
    for i in range(len(s)):
        # Add char to the count dict
        count[s[i]] += 1
        # key idea(2): Find the new max_count. This is much like Kadane's
        # Where we only consider if the new length exceedes the max_length overall
        max_count = max(max_count, count[s[i]])
        # Key idea (1): the answer is always max_count + k.
        if max_length < k + max_count:
            max_length += 1
        else:
            # key idea(3) This removes the char at the start of the subsequence s[i-max_length]
            # This serves as "correction" for the subsequence problem
            count[s[i - max_length]] -= 1
    return max_length





s = "AABABBAAABCDASAAASDA"
k = 2

res = characterReplacement(s, k)
