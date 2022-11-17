#


# first thought, TC:O(N), SC:O(N)
def firstUniqChar(s: str) -> int:
    check = [True] * len(s)
    memo = {}
    for i, l in enumerate(s):
        if l not in memo:
            memo[l] = i
        else:
            idx = memo[l]
            check[i] = False
            check[idx] = False
    for i, b in enumerate(check):
        if b: return i
    return -1
# use a counter, TC:O(N), SC:O(1)
def firstUniqChar2(s: str) -> int:
    counter = {}
    for l in s:
        counter[l] = counter.get(l, 0) + 1
    for i,l in enumerate(s):
        if counter[l] == 1:
            return i
    return -1