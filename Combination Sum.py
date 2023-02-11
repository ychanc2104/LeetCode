## https://leetcode.com/problems/combination-sum/
## https://leetcode.com/problems/combination-sum/discuss/937255/Python-3-or-DFSBacktracking-and-Two-DP-methods-or-Explanations


## dfs, backtracking, T: O(N*N^(M/min_cand)), min_cand=min(candidates), M=target, S:O(M/min_cand)
def combinationSum(candidates, target):
    """

    :param candidates: len N
    :param target:
    :return:
    """
    ans = []
    def dfs(target, index, path):
        #print(target, index, path)
        if target<0:
            return ## backtracking
        elif target==0:
            ans.append(path) ## an ans
            return
        for i in range(index, len(candidates)):
            dfs(target-candidates[i], i, path + [candidates[i]])
    dfs(target, 0, [])
    return ans

## dp (slow), T: O(M*M*M*N), S:O(M*M)
def combinationSum2(candidates, target):
    idx_d = {val: idx for idx, val in enumerate(candidates)}  # create {num:idx}
    n = len(candidates)
    dp = [[] for _ in range(target + 1)]
    for i in range(1, target + 1):  # from 1 to target, O(M)
        for j in range(i):  # O(M): for all previous calculated numbers
            for comb in dp[j]:  # O(M) worst: check each of their combinations
                start_idx = idx_d[comb[-1]]  # use start_idx to avoid repeats
                for val in candidates[start_idx:]:  # O(N): try all candidates
                    if val + j == i: dp[i].append(comb + [val])
        for candidate in candidates:  # O(N): directly from candidates not from previous result
            if candidate == i: dp[i].append([candidate])
    return dp[-1]

## dp (fast), T: O(M*M*N), S:O(M*M)
def combinationSum3(candidates, target):
    dp = [[] for _ in range(target+1)]
    for c in candidates:                                  # O(N): for each candidate
        for i in range(c, target+1):                      # O(M): for each possible value <= target
            if i == c: dp[i].append([c])
            for comb in dp[i-c]: dp[i].append(comb + [c]) # O(M) worst: for each combination
    return dp[-1]

# dfs, TC: O(N^(T/M+1)), M is min(candidates), SC:(T/M) for recursive calls
def combinationSum4(candidates, target: int):
    res = []
    def dfs(target, path):
        if target==0:
            res.append(path)
            return
        elif target<0:
            return
        # O(N)
        for num in candidates:
            # prevent double counting
            if not path or path[-1]>=num:
                # each iteration call dfs target/min(candidates) times
                dfs(target-num, path + [num])
    dfs(target, [])
    return res

## backtracking, T: O(N*N^(M/min_cand)), min_cand=min(candidates), M=target, S:O(M/min_cand)
def combinationSum5(candidates, target: int):
    path = []
    res = []
    def backtrack(target):
        if target == 0:
            res.append(path[:])
            return
        if target < 0:
            return
        for c in candidates:
            if path and path[-1] > c:
                continue
            path.append(c)
            backtrack(target - c)
            path.pop()
    backtrack(target)
    return res

## backtracking, T: O(N*N^(M/min_cand)), min_cand=min(candidates), M=target, S:O(M/min_cand)
def combinationSum6(candidates, target: int):
    # f(n) = [i] + temp for temp in dp[n-i]
    res = []
    path = []

    def backtrack(i, target):
        if target < 0 or i == len(candidates):
            return
        if target == 0:
            res.append(path[:])
            return
        num = candidates[i]
        path.append(num)
        backtrack(i, target - num)  # use
        path.pop()
        backtrack(i + 1, target)  # not used

    backtrack(0, target)
    return res