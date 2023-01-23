# https://leetcode.com/problems/palindrome-partitioning/



# first thought, backtracking, TC:O(N2^N), SC:O(N)
def partition(s: str) -> List[List[str]]:
    res = []
    sub = []

    def backtrack(i):
        if i == len(s):
            res.append(sub[:])

        for size in range(1, len(s) - i + 1):
            s_trial = s[i:i + size]
            # print(i, size, s_trial)
            if size != len(s_trial):
                continue
            if size == 1 or s_trial == s_trial[::-1]:  # valid
                sub.append(s_trial)
                backtrack(i + size)
                sub.pop()

    backtrack(0)
    return res