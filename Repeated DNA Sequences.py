# https://leetcode.com/problems/repeated-dna-sequences/description/


# first thought, TC:O((N-L)*L), SC:O((N-L)*L) for hash set
def findRepeatedDnaSequences(s: str) -> List[str]:
    memo = set()
    res = set()
    for i in range(len(s) - 9):
        sub = s[i:i + 10]
        if sub in memo:
            res.add(sub)
        else:
            memo.add(sub)
    return res


# Rabin-Karp, TC:O(N-L), SC:O(N-L)
def findRepeatedDnaSequences2(s: str) -> List[str]:
    if len(s) <= 10:
        return []
    # hash function,
    to_int = {'A': 0, 'T': 1, 'C': 2, 'G': 3}  # 4-numeral system
    h = 0
    for i in range(10):  # 0~9 pos
        h = h * 4 + to_int[s[i]]  # to numeral, SC:O(1)
    # hi = 4*h(i-1) + to_int[s[i]] - to_int[s[i-1]] * 4**10
    memo = set([h])
    res = set()
    for i in range(1, len(s) - 9):
        h = 4 * h - to_int[s[i - 1]] * 4 ** 10 + to_int[s[i + 9]]
        if h in memo:
            res.add(s[i:i + 10])
        else:
            memo.add(h)
    return res