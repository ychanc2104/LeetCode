# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/?envType=study-plan&id=binary-search-ii


# binary search to iterate every res, TC:O(NlogM), SC:O(1)
def minimumSize(nums: List[int], maxOperations: int) -> int:
    # split to n => take (num-1)/n
    def check(k): # TC:O(N)
        operations = 0
        for num in nums:
            operations += (num - 1) // k
        return operations

    # 2,4,8,2 => (1,8)4,1 => (move R) (1,3)2,4 => (move R) (1,1) 1,>4 => (move L) (2,1) stop
    L, R = 1, max(nums)
    while L <= R: # TC:O(logMax(nums))
        mid = (L + R) // 2
        if check(mid) <= maxOperations:
            R = mid - 1
        else:
            L = mid + 1
    return L