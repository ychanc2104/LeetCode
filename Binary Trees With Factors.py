# https://leetcode.com/problems/binary-trees-with-factors/description/

import math

# dp, TC:O(N^2), SC:O(N)
def numFactoredBinaryTrees(arr: List[int]) -> int:
    # find all common factor of i
    # 4 => 1*4 2*2 => [4], [4,2,2]
    MOD = 10 ** 9 + 7
    arr.sort()
    arr_set = set(arr)
    dp = {num: 1 for num in arr}  # initialize
    for i, num in enumerate(arr):
        for j in range(i):  # find all factors < arr[i]
            node1 = arr[j]
            if num % node1: continue  # valid node
            node2 = num // node1
            if node2 not in arr_set: continue  # another node should be in arr
            dp[num] += dp.get(node1, 1) * dp.get(node2, 1)
            dp[num] %= MOD
    return sum(dp.values()) % MOD

# modified dp, only compute to sqrt(num) and check left and right node equal or not, TC:O(N^2), SC:O(N)
def numFactoredBinaryTrees2(arr: List[int]) -> int:
    # find all common factor of i
    # 4 => 1*4 2*2 => [4], [4,2,2]
    MOD = 10**9 + 7
    arr.sort()
    arr_set = set(arr)
    dp = {num:1 for num in arr} # initialize
    for i, num in enumerate(arr):
        for j in range(i): # find all factors < arr[i], not include itself
            node1 = arr[j]
            if num % node1 or node1 > math.sqrt(num): continue # valid node
            node2 = num//node1
            if node2 not in arr_set: continue # another node should be in arr
            dp[num] += 2* dp[node1] * dp[node2] if node1 != node2 else dp[node1] * dp[node2]
            dp[num] %= MOD
    return sum(dp.values()) % MOD