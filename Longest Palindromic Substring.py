# https://leetcode.com/problems/longest-palindromic-substring/
# https://cppext.com/?p=1743




def longestPalindrome1(s):
    n = len(s)
    for i in range(n):
        for j in range(i + 1):
            s_test = s[j:n - i + j]
            if s_test == s_test[::-1]:
                return s_test


# https: // cppext.com /?p = 1743
def longestPalindrome3(s):  ## Manacher algorithm
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
def longestPalindrome4(s: str) -> str:
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
def longestPalindrome5(s: str) -> str:
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


# Manacher algorithm, TC:O(n), SC:(n)
def longestPalindrome6(s: str) -> str:
    T = '#'.join('^{}$'.format(s))
    n = len(T)
    P = [0] * n  # dp to store radius
    center = right_bound = 0
    maxI = maxRadius = 0
    for i in range(1,n - 1):
        if right_bound > i:  # not exceed
            # use mirror or right_bound - current_center(i)
            P[i] = min(P[center - (i - center)], right_bound - i)
        # start from P{i}+1 and P[i]-1
        while T[i - P[i] - 1] == T[i + P[i] + 1]:
            P[i] += 1
        if i + P[i] > right_bound:
            # update new center and right_bound
            center = i
            right_bound = P[i] + i
            # record max radius and its index
            if P[i] > maxRadius:
                maxI, maxRadius = i, P[i]
    return s[(maxI - maxRadius) // 2: (maxI + maxRadius) // 2]



# Manacher algorithm, TC:O(n), SC:(n)
def longestPalindrome7(s: str) -> str:
    sn = f"$#{'#'.join(s)}#^" # prevent boundary check
    dp = [0] * len(sn)
    C, R = 0, 0 # current center and radius
    mC, mR = 0, 0
    for i in range(1, len(sn)-1):
        # mirror x---C---i--|
        if i + dp[C-(i-C)] <= C + R:
            # safe
            dp[i] = min(dp[C-(i-C)], C + R - i)
        # center expansion
        while sn[i - dp[i] - 1] == sn[i + dp[i] + 1]:
            dp[i] += 1
        if i + dp[i] > C + R: # right bound
            C = i
            R = dp[i]
            if R > mR:
                mC, mR = C, R
    #print(sn,dp)
    return s[(mC - mR)//2 : (mC + mR)//2] # left bound to right bound


s = "aababa"


