# https://leetcode.com/problems/unique-paths/


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
    dp_map = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            dp_map[i][j] = dp_map[i-1][j] + dp_map[i][j-1]
    return dp_map[-1][-1]

# dp, 1D dp table(symmetry)
def uniquePaths5(m, n):
    dp=[1]*n
    for i in range(1,m):
        for j in range(1,n):
            dp[j]+=dp[j-1]
    return dp[-1]
# res = uniquePaths(20,12)

# res2 = uniquePaths2(8, 12)

res3 = uniquePaths3(8, 12)

res4 = uniquePaths4(8, 12)

res5 = uniquePaths5(1, 5)

m=3
n=5
dp = [1] * n
for i in range(1, m):
    print(i)
    for j in range(1, n):
        print(j)
        dp[j] += dp[j - 1]
