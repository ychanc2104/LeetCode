# https://leetcode.com/problems/combination-sum-ii/description/
# https://leetcode.com/problems/combination-sum-ii/solutions/750378/python3-dfs-solutions-templates-to-6-different-classic-backtracking-problems-more/

# backtracking, TC:O(N*2^N), SC:O(N) for recursive call and path
def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    path = []
    candidates.sort()

    def backtrack(pos, target):
        if target == 0:
            res.append(path[:])
            return
        if target < 0 or pos == len(candidates):
            return
        for i in range(pos, len(candidates)):
            if i > pos and candidates[i] == candidates[i - 1]: # key to prevent duplicates
                continue
            num = candidates[i]
            path.append(num)
            backtrack(i + 1, target - num)
            path.pop()

    backtrack(0, target)
    return res  # N*2^N