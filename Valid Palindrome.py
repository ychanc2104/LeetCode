# https://leetcode.com/problems/valid-palindrome/submissions/
# https://leetcode.com/problems/valid-palindrome/discuss/39982/Python-in-place-two-pointer-solution.

def isPalindrome(s: str) -> bool:
    s_clean = ''.join([a for a in s.lower() if (ord(a) >= 97 and ord(a) <= 122) or (ord(a) >= 48 and ord(a) <= 57)])
    return s_clean==s_clean[::-1]

# two pointer, O(n)
def isPalindrome2(s: str) -> bool:
    L, R = 0, len(s) - 1
    while L < R:
        if s[L].isalnum() and s[R].isalnum():
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        elif not s[L].isalnum():
            L += 1
        elif not s[R].isalnum():
            R -= 1
    return True