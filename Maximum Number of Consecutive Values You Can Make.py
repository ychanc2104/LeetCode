# https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description/
# https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/solutions/1118770/java-c-python-accumulate-the-coins/


# greedy, TC:O(NlogN), SC:O(N)
def getMaximumConsecutive(coins: List[int]) -> int:
    coins.sort()
    reach = 1
    for c in coins:
        if c > reach:
            return reach
        reach += c
    return reach