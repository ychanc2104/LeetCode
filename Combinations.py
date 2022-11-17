# https://leetcode.com/problems/combinations/
# https://leetcode.com/problems/combinations/discuss/27024/1-liner-3-liner-4-liner

# backtracking, TC:O(k*C(n,k)), SC:O(C(n,k))
def combine(n: int, k: int):
    res = []

    def backtrack(pos, path):
        if len(path) == k:
            # TC:O(k)
            res.append(path[:])
            # end
            return

        for i in range(pos, n):
            # add i+1 to path
            path.append(i + 1)
            # to next number
            backtrack(i + 1, path)
            # backtrack
            path.pop()

    backtrack(0, [])
    return res

# Lexicographic (binary sorted) combinations, TC:O(k*C(n,k)), SC:O(C(n,k))
def combine2(n: int, k: int):
    # init first combination
    nums = list(range(1, k + 1)) + [n + 1]

    output, j = [], 0
    while j < k:
        # add current combination
        output.append(nums[:k])
        # increase first nums[j] by one
        # if nums[j] + 1 != nums[j + 1]
        j = 0
        while j < k and nums[j + 1] == nums[j] + 1:
            nums[j] = j + 1
            j += 1
        nums[j] += 1

    return output

# iterative, TC:O(k*C(n,k)), SC:O()), SC is bad
def combine3(n, k):
    combs = [[]]
    for _ in range(k):
        combs = [[i] + c for c in combs for i in range(1, c[0] if c else n+1)]
    return combs

# iterative, TC:O(k*C(n,k)), SC:O(C(n,k)), SC is bad
def combine4(n, k):
    combs = [[i] for i in range(1, n+1)]
    for _ in range(k-1):
        temp = []
        for c in combs:
            # range(1, c[0]) => range(1,1)
            for i in range(1, c[0] if c else n + 1):
                temp.append([i] + c)
            print(combs, c, temp)
        combs = temp
    return combs


def combine5(n: int, k: int):
    res = []
    path = []
    def backtrack(pos):
        if len(path) == k:
            # TC:O(k)
            res.append(path[:])
            # end
            return

        for i in range(pos, n):
            # add i+1 to path
            path.append(i + 1)
            # to next number
            backtrack(i + 1)
            # backtrack
            path.pop()

    backtrack(0)
    return res

res = combine(4, 2)
res4 = combine5(4, 2)