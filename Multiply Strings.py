# https://leetcode.com/problems/multiply-strings/


# TC:O(NM), SC:O(N+M)
def multiply(num1: str, num2: str) -> str:
    if num1 == '0' or num2 == '0': return '0'
    memo = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    n, m = len(num1), len(num2)
    res = [0] * (n + m)
    # carry = 0
    # (3,456) 0,2 18,[0,0,1,8] => 0,1 15,[0,1,1+5,8] => 0,0 12,[1,1+2,6,8]
    # (13,456) 0,2 6,[0,1,3,6,8] => 1,1 15, => 1,0 12,
    for i in range(n - 1, -1, -1):  # (3,456) 0,2 18,[0,0,1,8] => 0,1 15,[0,1,1+5,8]
        l1 = num1[i]
        for j in range(m - 1, -1, -1):
            idx = i + j
            l2 = num2[j]
            carry = res[idx + 1]  # small digit
            mul = memo[l1] * memo[l2] + carry
            res[idx] += mul // 10  # add carry
            res[idx + 1] = mul % 10  # update digit
    res = ''.join(map(str, res))
    if res[0] == '0':
        return res[1:]
    return res