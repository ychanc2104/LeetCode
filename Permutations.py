# https://leetcode.com/problems/permutations/
# https://leetcode.com/problems/permutations/discuss/18296/Simple-Python-solution-(DFS).
import time
from functools import wraps

def timing(func):
    @wraps(func)
    def time_count(*args, **kwargs):
        t_start = time.time()
        values = func(*args, **kwargs)
        t_end = time.time()
        print (f"{func.__name__} time consuming:  {(t_end - t_start):.3f} seconds")
        return values
    return time_count


# first thought, TC: O(N^N)
def permute(nums):
    n = len(nums)
    res = []
    def dfs(path):
        if len(path) == n:
            res.append(path)

        for num in nums:
            # prevent double arranging
            # O(n)
            if num not in path:
                # call n times
                dfs(path + [num])
    dfs([])
    return res


# dfs, TC: O(N*(N!)^2), SC: O(N!) for recursive calls
def permute2(nums):
    n = len(nums)
    res = []
    def dfs(cands, path):
        if len(path)==n:
            res.append(path)
            return
        for i in range(len(cands)):
            # remove cands[i]
            # list slice, O(k)
            dfs(cands[:i] + cands[i+1:], path + [cands[i]])
    dfs(nums, [])
    return res

# dfs, TC: O(N*N!), SC: O(N!) for recursive calls
def permute3(nums):
    n = len(nums)
    output = []
    def backtrack(first=0):
        # if all integers are used up
        if first == n:
            # copy nums, O(N)
            output.append(nums[:])
        for i in range(first, n):
            # place i-th integer first
            # in the current permutation
            nums[first], nums[i] = nums[i], nums[first]
            # use next integers to complete the permutations
            backtrack(first + 1)
            # backtrack
            nums[first], nums[i] = nums[i], nums[first]
    backtrack(0)
    return output


nums = [1,3,5,7,9,11,13,15]
@timing
def test(n=1000):
    for i in range(n):
        res = permute(nums)
    return res

@timing
def test1(n=1000):
    for i in range(n):
        res = permute2(nums)
    return res

@timing
def test2(n=1000):
    for i in range(n):
        res = permute3(nums)
    return res

res = test(10)
res1 = test1(10)
res2 = test2(10)