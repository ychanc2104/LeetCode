# https://leetcode.com/problems/string-compression/description/


# TC:O(N), SC:O(1)
def compress(chars: List[str]) -> int:
    n = len(chars)
    L = R = 0
    i = 0
    while L < n:
        chars[i] = chars[L]
        i += 1
        while R < n and chars[L] == chars[R]:
            R += 1
        count = str(R - L)
        j = 0
        while R - L > 1 and j < len(count):
            chars[i] = count[j]
            i += 1
            j += 1
        L = R
    # while i < n:
    #     chars.pop()
    #     i += 1
    return i