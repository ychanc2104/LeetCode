# https://leetcode.com/problems/strobogrammatic-number/description/

# first thought, hash, TC:O(N), SC:O(N)
def isStrobogrammatic(num: str) -> bool:
    memo = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    res = []
    for c in num:
        if c not in memo:
            return False
        res.append(memo[c])
    return ''.join(res[::-1]) == num

# TC:O(N), SC:O(N)
def isStrobogrammatic2(num: str) -> bool:
    n = len(num)
    for i in range((n + 1) // 2):
        j = n - 1 - i
        if num[i] == '0' and num[j] == '0':
            continue
        if num[i] == '1' and num[j] == '1':
            continue
        if num[i] == '6' and num[j] == '9':
            continue
        if num[i] == '8' and num[j] == '8':
            continue
        if num[i] == '9' and num[j] == '6':
            continue
        return False
    return True