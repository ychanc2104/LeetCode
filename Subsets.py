# https://leetcode.com/problems/subsets/
# https://leetcode.com/problems/subsets/discuss/27301/Python-easy-to-understand-solutions-(DFS-recursively-Bit-Manipulation-Iteratively).


# first thought, dfs
def subsets(nums):
    res = [[]]
    def dfs(i, path):
        if len(path) >= 1 and path not in res:
            res.append(path)
        if i >= len(nums):
            return
        dfs(i + 1, path + [nums[i]])
        dfs(i + 1, path)
    dfs(0, [])
    return res


# TC:O(N*2^N), SC:O(N*2^N)
def subsets2(nums):
    res = [[]]
    for num in nums:
        # add num to existing res
        # [] => [],[1] => [],[1],[2],[1,2] =>...
        # extend take O(n)
        res += [c + [num] for c in res]
    return res


# dfs
def subsets3(nums):
    res = []
    def dfs(nums, path):
        res.append(path)
        for i in range(len(nums)):
            dfs(nums[i + 1:], path + [nums[i]])
    dfs(nums, [])
    return res

# backtracking
def subsets4(nums):
    res = []

    def backtracking(l, i, path):
        # l: desired length
        if l == len(path):
            res.append(path)
            return
        if i >= len(nums):
            return
        # pick
        backtracking(l, i + 1, path + [nums[i]])
        # not pick
        backtracking(l, i + 1, path)

    for i in range(len(nums) + 1):
        # iterate all desired length, 0 to len(nums)
        backtracking(i, 0, [])
    return res