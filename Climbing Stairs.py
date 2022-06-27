# https://leetcode.com/problems/climbing-stairs/

# dp, TC:O(n), SC:O(1)
def climbStairs(n: int) -> int:
    # n = 1, 1
    # n = 2, 2
    f0 = 0
    f1 = 1
    for i in range(n):
        f2 = f0 + f1
        f0, f1 = f1, f2
    return f2