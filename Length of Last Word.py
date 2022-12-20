# https://leetcode.com/problems/length-of-last-word/


# TC:O(N), SC:O(1)
def lengthOfLastWord(s: str) -> int:
    res = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ':
            if res == 0:
                continue
            else:
                break
        else:
            res += 1
    return res