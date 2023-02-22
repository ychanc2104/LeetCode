# https://leetcode.com/problems/string-compression-ii/description/
# https://leetcode.com/problems/string-compression-ii/solutions/2704470/leetcode-the-hard-way-explained-line-by-line/

import functools

def getLengthOfOptimalCompression(s: str, k: int) -> int:
    @functools.lru_cache(None)
    def dp(i, k, prev, prev_count):
        # aaabcccd, 2 =>
        if k < 0:  # don't delete anymore
            return float("inf")
        if i == len(s):
            return 0
        ## compare delete and keep the char
        delete = dp(i + 1, k - 1, prev, prev_count)
        if s[i] == prev:
            # consecutive char, aaa
            keep = dp(i + 1, k, prev, prev_count + 1)
            if prev_count in [1, 9, 99]:
                keep += 1
        else:
            # another char
            keep = dp(i + 1, k, s[i], 1) + 1
        return min(keep, delete)

    return dp(0, k, '', 0)



def getLengthOfOptimalCompression2(s: str, k: int) -> int:
    @functools.lru_cache(None)
    def helper(i, k, prev='', count=0):
        if i == len(s):
            return 0
        char = s[i]
        res1 = res2 = res3 = float('inf')
        if prev == char:
            res1 = helper(i+1, k, prev, count+1) + (1 if count==1 or count == 9 or count == 99 else 0)
        else:
            # delete
            if k > 0:
                res2 = helper(i+1, k-1, prev, count)
            res3 = helper(i+1, k, char, 1) + 1
        return min(res1, res2, res3)

    return helper(0, k)