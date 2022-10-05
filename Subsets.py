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


# backtracking, TC:O(N*2^N), SC:O(N)
def subsets4(nums):
    res = []
    path = []
    def backtrack(pos):
        if pos == len(nums):
            res.append(path[:]) # TC:O(N)
            return
        path.append(nums[pos])
        backtrack(pos + 1)  # choose
        path.pop()
        backtrack(pos + 1)  # not choose

    backtrack(0)
    return res