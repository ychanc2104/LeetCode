# https://leetcode.com/problems/non-decreasing-subsequences/description/
# https://leetcode.com/problems/restore-ip-addresses/solutions/31140/python-easy-to-understand-solution-backtracking/

# first thought, dfs+dp, TC:O(), SC:O(N2^N)
def findSubsequences(nums: List[int]) -> List[List[int]]:
    memo = {}

    def dfs(i=0):  # res of nums[i:], i=0,1,2,...,n-2
        if i in memo:
            return memo[i]
        res = set()
        for j in range(i, len(nums) - 1):
            if nums[i] <= nums[j + 1]:
                res.add((nums[i], nums[j + 1]))
                for sub in dfs(j + 1):
                    res.add(tuple([nums[i]] + list(sub)))
        memo[i] = res
        return res

    for i in range(len(nums)):
        dfs(i)
    # print(memo)
    res = set()
    for s in memo.values():
        res = res.union(s)
    return res


# backtracking, TC:O(N2^N), SC:O(N) for recursive call
def findSubsequences2(nums: List[int]) -> List[List[int]]:
    sub = []
    res = set()
    def backtrack(i):
        if i == len(nums):
            if len(sub) > 1:
                res.add(tuple(sub[:]))
            return

        # add or not add
        if not sub or nums[i] >= sub[-1]:
            sub.append(nums[i])
            backtrack(i+1)
            sub.pop()
        backtrack(i+1)

    backtrack(0)
    return res

# backtracking, TC:O(N2^N), SC:O(N) for recursive call
def findSubsequences3(nums: List[int]) -> List[List[int]]:
    sub = []
    res = set()
    def backtrack(i):
        if len(sub) > 1:
            res.add(tuple(sub[:]))

        # add or not add
        for j in range(i, len(nums)):
            if not sub or nums[j] >= sub[-1]:
                sub.append(nums[j])
                backtrack(j+1)
                sub.pop()

    backtrack(0)
    return res