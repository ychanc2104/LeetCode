# https://leetcode.com/problems/find-the-divisibility-array-of-a-string/description/


# TC:O(N), SC:O(1)
def divisibilityArray(word: str, m: int) -> List[int]:
    res = []
    rem = 0
    for d in word:
        rem = (rem * 10 + int(d)) % m
        res.append(1 if not rem else 0)
    return res