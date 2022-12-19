# https://leetcode.com/problems/repeated-substring-pattern/description/
# https://leetcode.com/problems/repeated-substring-pattern/solutions/826121/python-2-solutions-1-oneliner-explained/

def repeatedSubstringPattern(s: str) -> bool:
    n = len(s)
    for i in range(1, n // 2 + 1):  # window size
        pattern = s[:i]
        if n % i != 0: continue
        for j in range(i, n, i):
            if s[j:j + i] != pattern:
                break
        else:
            return True
    return False

# s=pp, pp in xppy, TC:O(N), SC:O(N)
def repeatedSubstringPattern2(s: str) -> bool:
    return s in (s+s)[1:-1]