# https://leetcode.com/problems/3sum-closest/


# first thought, TC:O(3*n!/(3!*(n-3)!))
def threeSumClosest(nums: List[int], target: int) -> int:
    res = [float("inf")]
    # combination, n!/(3!*(n-3)!)
    def backtrack(pos, path):
        if len(path) == 3:
            pathSum = sum(path)
            if (pathSum == target or abs(target - pathSum) < abs(target - res[0])):
                res[0] = pathSum
            return
        # -1,2,1 =>
        for i in range(pos, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return res[0]


# like 3 sum, two-pointer, TC:O(n^2), SC:(n) in timsort
def threeSumClosest2(nums: List[int], target: int) -> int:
    diff = float("inf")
    nums.sort()
    for i in range(len(nums)):
        L, R = i+1, len(nums)-1
        while L < R:
            tempSum = nums[i] + nums[L] + nums[R]
            if abs(tempSum - target) < abs(diff):
                diff = tempSum - target
            if target == tempSum:
                return target
            elif tempSum < target:
                # move L to bigger
                L += 1
            else:
                # move R to smaller
                R -= 1
    return target + diff
