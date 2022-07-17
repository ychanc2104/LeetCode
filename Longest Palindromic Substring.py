# https://leetcode.com/problems/longest-palindromic-substring/
# https://cppext.com/?p=1743


class Solution:
    def __init__(self, s):
        self.ans_1 = self.longestPalindrome_1(s)
        self.ans_2 = self.longestPalindrome_2(s)

    def longestPalindrome_1(self, s):
        n = len(s)
        for i in range(n):
            for j in range(i + 1):
                s_test = s[j:n - i + j]
                if s_test == s_test[::-1]:
                    return s_test
    def longestPalindrome_2(self, s): ## Manacher algorithm
        ## https://havincy.github.io/blog/post/ManacherAlgorithm/
        ## calculate palindromic radius
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        Imax = 0
        radius = 0
        for i in range(n-1):
            j = 0
            while T[i-(j+1)] == T[i+(j+1)]:
                P[i] += 1
                j += 1
            if i != 0 and P[i] > radius:
                Imax = i
                radius = P[i]
        s_sub = s[(Imax-radius)//2:(Imax+radius)//2]
        return s_sub

    # https: // cppext.com /?p = 1743
    def longestPalindrome_3(self, s):  ## Manacher algorithm
    # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            P[i] = (R > i) and min(R - i, P[C-(i-C)])  # equals to i' = C - (i-C), mirror pos
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]


# expand around center, TC:O(n^2), SC:(1)
def longestPalindrome(s: str) -> str:
    resL = 0
    center = 0
    # len = n + n-1 = 2n-1
    s = '#'.join(s)
    # R = 1
    for i in range(len(s)):
        R = 0
        while i-R>=0 and i+R<len(s) and s[i-R]==s[i+R]:
            # print(s[i-R],s[i],s[i+R])
            if s[i]=='#' and R%2==1 and R+1 > resL:
                # a#a(1), #a#a#(2), when R is odd
                center = i
                resL = R+1
            elif s[i]!='#' and R%2==0 and R+1 > resL:
                center = i
                resL = R+1
            R += 1
    return s[center-resL+1:center+resL].replace('#', '')

# Manacher algorithm, TC:O(n), SC:(n)
def longestPalindrome2(s: str) -> str:
# Transform S into T.
    # For example, S = "abba", T = "^#a#b#b#a#$".
    # ^ and $ signs are sentinels appended to each end to avoid bounds checking
    T = f"^#{'#'.join(s)}#$"
    n = len(T)
    P = [0] * n
    C = R = 0 # C is center, R is rightmost position
    for i in range(1, n-1):
        #print(i, P)
        if R > i:
            # do not exceed R-i (radius of pos i)
            # C - (i-C) is the left mirror pos
            P[i] = min(P[C-(i-C)], R-i)
        # Attempt to expand palindrome centered at i
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1

        # If palindrome centered at i expand past R,
        # adjust center based on expanded palindrome.
        if i + P[i] > R:
            C, R = i, i + P[i]
    # Find the maximum element in P.
    maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
    #return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]
    return T[centerIndex - maxLen+1:centerIndex + maxLen].replace('#', '')


s = "aababa"
A = Solution(s)
