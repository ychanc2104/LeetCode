# https://leetcode.com/problems/reverse-bits/
# https://leetcode.com/problems/reverse-bits/discuss/732138/Python-O(32)-simple-solution-explained


def reverseBits(n: int) -> int:
    ans = 0
    for i in range(32):
        # (n&1) is 1 or 0
        ans = (n & 1) + (ans << 1)
        n = n >> 1
    return ans

def reverseBits2(n: int) -> int:
    ans = 0
    for i in range(32):
        # exclusive or
        ans = (n & 1)^(ans << 1)
        n = n >> 1
    return ans

def reverseBits3(n: int) -> int:
    ans = 0
    for i in range(32):
        # or
        ans = (n & 1)|(ans << 1)
        n = n >> 1
    return ans