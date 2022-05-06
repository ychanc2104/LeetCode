## https://leetcode.com/problems/combination-sum/
## https://leetcode.com/problems/combination-sum/discuss/937255/Python-3-or-DFSBacktracking-and-Two-DP-methods-or-Explanations


class Solution:
    ## dfs, backtracking, T: O(N*N^(M/min_cand)), min_cand=min(candidates), M=target, S:O(M/min_cand)
    def combinationSum(self, candidates, target):
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
    def combinationSum2(self, candidates, target):
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
    def combinationSum3(self, candidates, target):
        dp = [[] for _ in range(target+1)]
        for c in candidates:                                  # O(N): for each candidate
            for i in range(c, target+1):                      # O(M): for each possible value <= target
                if i == c: dp[i].append([c])
                for comb in dp[i-c]: dp[i].append(comb + [c]) # O(M) worst: for each combination
        return dp[-1]