# https://leetcode.com/problems/unique-paths/
# https://leetcode.com/problems/unique-paths/discuss/254228/Python-3-solutions%3A-Bottom-up-DP-Math-Picture-Explained-Clean-and-Concise
# https://bugs.python.org/issue8692

def uniquePaths(m, n):
    start = [0, 0]
    queue = [start]
    res = 0
    while queue:
        pos = queue.pop(0)
        if pos == [m - 1, n - 1]:
            res += 1
        else:
            # down
            if pos[0] < m - 1:
                queue.append([pos[0] + 1, pos[1]])
            # right
            if pos[1] < n - 1:
                queue.append([pos[0], pos[1] + 1])
    return res

## recursive
def uniquePaths2(m, n):
    if m == 0 or n == 0:
        return 0
    elif m==1 or n==1:
        return 1
    elif m==2 or n==2:
        return max(m,n)
    else:
        return uniquePaths(m, n - 1) + uniquePaths(m - 1, n)


## dp
def uniquePaths3(m, n):
    dict_map = {}
    for i in range(2, m + 1):
        for j in range(2, n + 1):
            f1 = 1 if i == 2 or j == 1 else dict_map[f"{i - 1},{j}"]
            f2 = 1 if i == 1 or j == 2 else dict_map[f"{i},{j - 1}"]
            dict_map[f"{i},{j}"] = 1 if i == 1 or j == 1 else f1+f2
    return 1 if m == 1 or n == 1 else dict_map[f"{m},{n}"]

## dp
def uniquePaths4(m, n):
    # dp[m][n] = dp[m-1][n] + dp[m][n-1], dp[m][1] = 1, dp[1][n] = 1
    dp_map = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            dp_map[i][j] = dp_map[i-1][j] + dp_map[i][j-1]
    return dp_map[-1][-1]

# dp, 1D dp table(symmetry)
def uniquePaths5(m, n):
    # dp([m])[n] = dp([m-1])[n] + dp([m])[n-1], 1D dp, hidden m, dp[0] = 1
    dp=[1]*n
    for i in range(1,m):
        for j in range(1,n):
            dp[j] += dp[j-1]
    return dp[-1]

# math, There are (h+v) total moves, once choose v steps or h steps, one choice remains
# res = C(h+v, h) = (h+v)!/h!v!, h = n - 1(cols) and v = m - 1(rows)
def uniquePaths6(m, n):
    # k! can be computed in O(k(log⁡klog⁡log⁡k)^2) time.
    return math.factorial(n+m-2)//math.factorial(n-1)//math.factorial(m-1)


