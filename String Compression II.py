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