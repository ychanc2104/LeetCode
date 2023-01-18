# https://leetcode.com/problems/flip-string-to-monotone-increasing/description/

# dp, TC:O(N), SC:O(1)
def minFlipsMonoIncr(s: str) -> int:
    counter_flip, counter_one = 0, 0
    for e in s:
        if e == '0':
            # answer is (flipping current 0 + previous answer) or (flipping all previous 1)
            counter_flip = min(counter_flip + 1, counter_one)
        else:
            counter_one += 1
    return counter_flip