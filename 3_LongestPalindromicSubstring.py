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

    def longestPalindrome_3(self, s):  ## Manacher algorithm
    # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            P[i] = (R > i) and min(R - i, P[2 * C - i])  # equals to i' = C - (i-C)
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


s = "aababa"
A = Solution(s)

T = '#'.join('^{}$'.format(s))
n = len(T)
P = [0] * n
C = R = 0
for i in range(1, n - 1):
    P[i] = (R > i) and min(R - i, P[2 * C - i])  # equals to i' = C - (i-C)
    # Attempt to expand palindrome centered at i
    while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
        P[i] += 1

    # If palindrome centered at i expand past R,
    # adjust center based on expanded palindrome.
    if i + P[i] > R:
        C, R = i, i + P[i]

# Find the maximum element in P.
maxLen, centerIndex = max((n, i) for i, n in enumerate(P))

output = s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]

T = '#'.join('^{}$'.format(s))
n = len(T)
P = [0] * n
Imax = 0
radius = 0
for i in range(n - 1):
    j = 0
    while T[i - (j + 1)] == T[i + (j + 1)]:
        P[i] += 1
        j += 1
    if i != 0 and P[i] > radius:
        Imax = i
        radius = P[i]