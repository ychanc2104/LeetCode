# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/


# first thought, TC:O(min(N,M)*(N+M)), SC:O(N+M)
def gcdOfStrings(str1: str, str2: str) -> str:
    # common pattern
    n1, n2 = len(str1), len(str2)
    if n1 < n2:
        return gcdOfStrings(str2, str1)
    for i in range(n2, 0, -1):
        sub = str2[:i]
        if sub * (n1 // i) == str1 and sub * (n2 // i) == str2:
            return sub
    return ""

# TC:O(N+M) for comparison, SC:O(N+M) for comparison
def gcdOfStrings2(str1: str, str2: str) -> str:
    # must from its gcd of len1 and len2
    def gcd(n, m):
        if m == 0:
            return n
        return gcd(m, n % m)

    n1, n2 = len(str1), len(str2)
    if str1 + str2 == str2 + str1:
        return str1[:gcd(n1, n2)]
    return ""